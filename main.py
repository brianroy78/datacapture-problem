from models import DataCapture


def main():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.less(4))


if __name__ == '__main__':
    main()
