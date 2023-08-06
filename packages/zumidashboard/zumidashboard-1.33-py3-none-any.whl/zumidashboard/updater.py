from zumi.zumi import Zumi
from zumi.util.screen import Screen
import time

import os, subprocess, time, signal
from threading import Thread
from PIL import Image, ImageDraw
import numpy as np


def __progress(screen, img, start, end):
    while start != end:
        draw = ImageDraw.Draw(img)
        draw.point([(start + 13, 35), (start + 13, 36), (start + 13, 37)])
        screen.draw_image(img.convert('1'))
        start += 1


def __finished_updating(_screen, text):
    _zumi = Zumi()
    img = _screen.path_to_image('/usr/local/lib/python3.5/dist-packages/zumi/util/images/happy1.ppm')
    time.sleep(.5)
    _screen.draw_text(text, x=10, y=5, image=img.convert('1'), font_size=12, clear=False)

    tempo = 60
    time.sleep(0.5)
    _zumi.play_note(41, tempo)
    _zumi.play_note(43, tempo)
    _zumi.play_note(45, tempo)


def __kill_updater(proc, timeout):
    print("timeout!")
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    timeout["value"] = True


def update_version(_screen):
    p = subprocess.Popen('sudo pip3 install zumidashboard --upgrade',
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    img_arr = np.asarray(Image.open('/usr/local/lib/python3.5/dist-packages/zumi/util/images/blankbar.ppm'))
    img = Image.fromarray(img_arr.astype('uint8'))

    _screen.draw_text("Updating Firmware", x=9, y=8, image=img.convert('1'), font_size=12, clear=False)
    img = _screen.screen_image.convert('RGB')

    updater_thread = Thread(target=__progress, args=(_screen,img, 0, 51))
    updater_thread.start()

    try:
        while p.poll() is None:
            line = p.stdout.readline().decode()
            print(line)

            if 'Error' in line:
                _screen.draw_text_center("Error!\nPlease Try Again")
                return

            if 'Collecting' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 51, 88))
                updater_thread.start()

            elif 'Installing collected packages' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 88, 96))
                updater_thread.start()

            elif 'Successfully installed' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 96, 101))
                updater_thread.start()
                version_info = line.split('-')[-1]

        print(version_info)
        updater_thread.join()

        time.sleep(1)
        __finished_updating(_screen, "Firmware updated!")
        _screen.draw_text_center("Firmware updated to v" + str(version_info), font_size=15)

    except Exception as e:
        updater_thread.join()
        _screen.draw_text_center("Zumi firmware is already latest")
        print(e)


def update_content(_screen):
    current = open('/home/pi/Zumi_Content/README.md').readline().split()[0]
    past_folder = 'mv /home/pi/Zumi_Content /home/pi/log_v'+str(current+'_content')
    print(past_folder)
    cnt = 1
    while os.path.isdir(past_folder.split(' ')[2]):
        past_folder+='_{}'.format(cnt)
        cnt+=1
        print(past_folder)
    subprocess.Popen(past_folder,
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    time.sleep(1)
    past_folder = "sudo chown -R pi /home/pi/" + past_folder
    
    subprocess.Popen(past_folder,
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    print("change name ")
    p = subprocess.Popen(
        'git clone https://github.com/RobolinkInc/Zumi_Content /home/pi/Zumi_Content',
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, preexec_fn=os.setsid)

    img_arr = np.asarray(Image.open('/usr/local/lib/python3.5/dist-packages/zumi/util/images/blankbar.ppm'))
    img = Image.fromarray(img_arr.astype('uint8'))
    print("start clone")
    _screen.draw_text("Updating Content", x=12, y=8, image=img.convert('1'), font_size=12, clear=False)
    img = _screen.screen_image.convert('RGB')

    time.sleep(1)
    content_updater_thread = Thread(target=__progress, args=(_screen, img, 0, 101))
    while p.poll() is None:
        line = p.stdout.readline().decode()
        print(line)

        if 'Cloning into ' in line:
            content_updater_thread.start()

        elif 'Already up-to-date' in line:
            _screen.draw_text_center('Zumi content is already latest')
            break
    try:
        content_updater_thread.join()
    except Exception as e:
        print(e)
        print("error")
        _screen.draw_text_center("Fail to update content")
        return False
    time.sleep(1)
    subprocess.Popen("sudo chown -R pi /home/pi/Zumi_Content",
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    update_lessonlist_file()
    __finished_updating(_screen, "Content updated!")
    time.sleep(3)
    return True


def restart_threads(_screen):
    Thread(target=restart_app, args=()).start()
    Thread(target=go_to_zumi_dashboard_msg, args=(_screen,)).start()


def restart_app():
    subprocess.run(["sudo python3 /home/pi/Dashboard/dashboard.py"], shell=True)


def go_to_zumi_dashboard_msg(_screen):
    _screen.draw_text_center("Dashboard restarting...")
    for x in range(20):
        time.sleep(1)
    _screen.draw_text_center("Go to \"zumidashboard.ai\" in your browser")


def check_content_version():
    new = os.popen("curl -m 12 --fail https://raw.githubusercontent.com/RobolinkInc/Zumi_Content/master/README.md").read().split()[0]
    current = open('/home/pi/Zumi_Content/README.md').readline().split()[0]
    if new == current:
        return True
    else:
        return False


def update_lessonlist_file():
    import json

    lesson_files_path = "/home/pi/Zumi_Content/Lesson/"
    lesson_file_list = os.listdir(lesson_files_path)
    lesson_file_list.sort()

    lesson_list = []

    lesson_id = 0
    for lesson_name in lesson_file_list:
        if lesson_name != '.ipynb_checkpoints':
            with open(lesson_files_path + lesson_name, 'r') as lesson_file:
                file_content = json.loads(lesson_file.read())
            try:
                description = file_content["cells"][1]["source"][2].split(">")[1].split("<")[0].replace("\n", " ")

                if len(description) > 175:
                    description = description[:175] + "..."
            except:
                description = " "
            lesson_info = {"id": lesson_id, "title": lesson_name[:-6], "description": description}
            lesson_list.append(lesson_info)
            lesson_id = lesson_id + 1

    lesson_list_json = {"LessonList": lesson_list}

    with open('/usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/LessonList.json', 'w') as lesson_list_file:
        json.dump(lesson_list_json, lesson_list_file)


def update_eveything_pipeline(_screen):
    update_version(_screen)
    time.sleep(2)
    update_content(_screen)
    restart_threads(_screen)


def update_dashboard_pipeline(_screen):
    update_version(_screen)
    time.sleep(2)
    restart_threads(_screen)


def run():
    screen = Screen(clear=False)
    update_dashboard_pipeline(screen)


def run_everything():
    screen = Screen(clear=False)
    update_eveything_pipeline(screen)


if __name__ == '__main__':
    run()

