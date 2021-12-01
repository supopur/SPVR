import usb.core
import usb.util

def main(mode : str, ):
    devList = usb.core.find(find_all=True)
    print(devList)
if __name__ == "__main__":
    main('test')