#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import argparse
import asyncio
import concurrent.futures
import logging
import sys
from typing import List, Optional, Set

import idb.common.plugin as plugin
from idb.cli.commands.accessibility import (
    AccessibilityInfoAllCommand,
    AccessibilityInfoAtPointCommand,
)
from idb.cli.commands.add_media import AddMediaCommand
from idb.cli.commands.app import (
    AppInstallCommand,
    AppTerminateCommand,
    AppUninstallCommand,
)
from idb.cli.commands.approve import ApproveCommand
from idb.cli.commands.boot import BootCommand
from idb.cli.commands.clear_keychain import ClearKeychainCommand
from idb.cli.commands.connect import ConnectCommand, ConnectCommandException
from idb.cli.commands.contacts import ContactsUpdateCommand
from idb.cli.commands.crash import (
    CrashDeleteCommand,
    CrashListCommand,
    CrashShowCommand,
)
from idb.cli.commands.daemon import DaemonCommand
from idb.cli.commands.debugserver import (
    DebugServerStartCommand,
    DebugServerStatusCommand,
    DebugServerStopCommand,
)
from idb.cli.commands.describe import DescribeCommand
from idb.cli.commands.disconnect import DisconnectCommand
from idb.cli.commands.dsym import DsymInstallCommand
from idb.cli.commands.dylib import DylibInstallCommand
from idb.cli.commands.file import (
    DeprecatedPullCommand,
    DeprecatedPushCommand,
    FSListCommand,
    FSMkdirCommand,
    FSMoveCommand,
    FSPullCommand,
    FSPushCommand,
    FSRemoveCommand,
)
from idb.cli.commands.focus import FocusCommand
from idb.cli.commands.framework import FrameworkInstallCommand
from idb.cli.commands.hid import (
    ButtonCommand,
    KeyCommand,
    KeySequenceCommand,
    SwipeCommand,
    TapCommand,
    TextCommand,
)
from idb.cli.commands.instruments import InstrumentsCommand
from idb.cli.commands.kill import KillCommand
from idb.cli.commands.launch import LaunchCommand
from idb.cli.commands.list_apps import ListAppsCommand
from idb.cli.commands.list_targets import ListTargetsCommand
from idb.cli.commands.log import CompanionLogCommand, LogCommand
from idb.cli.commands.open_url import OpenUrlCommand
from idb.cli.commands.record import RecordVideoCommand
from idb.cli.commands.screenshot import ScreenshotCommand
from idb.cli.commands.set_location import SetLocationCommand
from idb.cli.commands.xctest import (
    XctestInstallCommand,
    XctestListTestsCommand,
    XctestRunCommand,
    XctestsListBundlesCommand,
)
from idb.common.command import Command, CommandGroup
from idb.common.types import IdbException


COROUTINE_DRAIN_TIMEOUT = 2


# Set the logger's basicConfig first, then add the logview handlers
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] - %(name)s - %(message)s"
)
logger: logging.Logger = logging.getLogger()


async def gen_main(cmd_input: Optional[List[str]] = None,) -> int:
    # Setup parser
    parser = argparse.ArgumentParser(
        description="idb: a versatile tool to communicate with iOS Simulators and Devices",
        epilog="See Also: https://www.fbidb.io/docs/guided-tour",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    commands: List[Command] = [
        DescribeCommand(),
        AppInstallCommand(),
        AppUninstallCommand(),
        ListAppsCommand(),
        LaunchCommand(),
        AppTerminateCommand(),
        CommandGroup(
            name="xctest",
            description="Operations with xctest on target",
            commands=[
                XctestInstallCommand(),
                XctestsListBundlesCommand(),
                XctestListTestsCommand(),
                XctestRunCommand(),
            ],
        ),
        CommandGroup(
            name="file",
            description="File operations on target",
            commands=[
                FSMoveCommand(),
                FSPullCommand(),
                FSPushCommand(),
                FSMkdirCommand(),
                FSRemoveCommand(),
                FSListCommand(),
            ],
        ),
        CommandGroup(
            name="contacts",
            description="Contacts database operations on target",
            commands=[ContactsUpdateCommand()],
        ),
        LogCommand(),
        CommandGroup(
            name="record",
            description="Record what the screen is doing",
            commands=[RecordVideoCommand()],
        ),
        RecordVideoCommand(),
        DeprecatedPushCommand(),
        DeprecatedPullCommand(),
        OpenUrlCommand(),
        ClearKeychainCommand(),
        SetLocationCommand(),
        ApproveCommand(),
        ConnectCommand(),
        DisconnectCommand(),
        ListTargetsCommand(),
        DaemonCommand(),
        ScreenshotCommand(),
        CommandGroup(
            name="ui",
            description="UI interactions on target",
            commands=[
                AccessibilityInfoAllCommand(),
                AccessibilityInfoAtPointCommand(),
                TapCommand(),
                ButtonCommand(),
                TextCommand(),
                KeyCommand(),
                KeySequenceCommand(),
                SwipeCommand(),
            ],
        ),
        CommandGroup(
            name="crash",
            description="Operations on crashes",
            commands=[CrashListCommand(), CrashShowCommand(), CrashDeleteCommand()],
        ),
        InstrumentsCommand(),
        KillCommand(),
        AddMediaCommand(),
        FocusCommand(),
        BootCommand(),
        CommandGroup(
            name="debugserver",
            description="debugserver interactions",
            commands=[
                DebugServerStartCommand(),
                DebugServerStopCommand(),
                DebugServerStatusCommand(),
            ],
        ),
        CommandGroup(
            name="dsym", description="dsym commands", commands=[DsymInstallCommand()]
        ),
        CommandGroup(
            name="dylib", description="dylib commands", commands=[DylibInstallCommand()]
        ),
        CommandGroup(
            name="framework",
            description="framework commands",
            commands=[FrameworkInstallCommand()],
        ),
        CommandGroup(
            name="companion",
            description="commands related to the companion",
            commands=[CompanionLogCommand()],
        ),
    ]
    commands.extend(plugin.get_commands())
    sorted_commands = sorted(commands, key=lambda command: command.name)
    root_command = CommandGroup("root_command", "", sorted_commands)
    root_command.add_parser_arguments(parser)

    # Parse input and run
    cmd_input = cmd_input or sys.argv[1:]

    try:
        args = parser.parse_args(cmd_input)
        plugin.on_launch(logger)
        await root_command.run(args)
        return 0
    except ConnectCommandException as e:
        print(str(e))
        return 1
    except IdbException as e:
        print(e.args[0])
        return 1
    except Exception:
        logger.exception("Exception thrown in main")
        return 1
    finally:
        await plugin.on_close(logger)
        pending = set(asyncio.Task.all_tasks())
        pending.discard(asyncio.Task.current_task())
        await drain_coroutines(pending)


async def drain_coroutines(pending: Set[asyncio.Task]) -> None:
    if not pending:
        return
    logger.debug(f"Shutting down {len(pending)} coroutines")
    try:
        await asyncio.wait_for(
            asyncio.shield(asyncio.gather(*pending)), timeout=COROUTINE_DRAIN_TIMEOUT
        )
        logger.debug(f"Drained all coroutines")
    except asyncio.TimeoutError:
        logger.debug(f"Timeout waiting for coroutines to drain")
    except concurrent.futures.CancelledError:
        pass


def main(cmd_input: Optional[List[str]] = None,) -> int:
    loop = asyncio.get_event_loop()
    try:
        return loop.run_until_complete(gen_main(cmd_input))
    finally:
        loop.close()


if __name__ == "__main__":
    sys.exit(main())
