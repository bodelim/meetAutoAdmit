import pyautogui
import time

print("[AutoAdmit] 프로그램 준비완료.")

def main():
    try:
        pyautogui.click('admitButton.png')
        print("[AutoAdmit] 성공적으로 수락하였습니다.")
        time.sleep(0.2)
        main()
        return
    except:
        print("[AutoAdmit] 감지안됨.")
        time.sleep(0.2)
        main()
        return

main()
