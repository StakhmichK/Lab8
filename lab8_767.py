def open_file(filename):
    try:
        f = open(filename, "r", encoding="utf-8")
        print("OK")
        f.close()
    except IOError:
        print("Caught the I/O error")
    finally:
        print("Done")
open_file("data/input_767_1.txt")
open_file("data/input_767_2.txt")
open_file("data/input_767_3.txt")