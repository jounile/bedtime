from timer import MyMainWindow

def main():
    try:
        MyMainWindow.__init__()
    finally:
        print("Done")

if __name__ == "__main__":
    main()

