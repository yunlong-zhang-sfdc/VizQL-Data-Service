import asyncio
import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import src.examples.async_examples as async_examples
import src.examples.common as common
import src.examples.sync_examples as sync_examples

if __name__ == "__main__":
    # Check for help flag before parsing arguments
    if "-h" in sys.argv or "--help" in sys.argv:
        common.print_help()
        sys.exit(0)

    parser = common.parse_arguments()
    parser.add_argument(
        "--async",
        dest="async_mode",
        action="store_true",
        help="Run examples in async mode",
    )
    args = parser.parse_args()

    if args.async_mode:
        asyncio.run(async_examples.execute(args))
    else:
        sync_examples.execute(args)
