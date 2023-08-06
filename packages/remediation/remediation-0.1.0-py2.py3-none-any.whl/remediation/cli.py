"""Console script for remediation."""
import argparse
import sys
from remediation.data_generators import CM11Generator as CM11


def main():
    """
    Console script for remediation.

    - generates fake date
    - populate a database with generated fake data

    """

    # print(sys.path)

    parser = argparse.ArgumentParser(
        description="Tool to support remediation activities, \
             reporting, monitoring, ...")
    parser.add_argument('-n', '--num_data',
                        dest='n',
                        action='store',
                        default=10,
                        type=int)
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    cm11_gen = CM11(args.n)

    data = cm11_gen.get_generated_data_as_list_of_dict()
    print(data)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
