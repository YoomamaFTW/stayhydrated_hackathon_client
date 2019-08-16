import PySimpleGUI as sg
# TO align in center, use justification='center'


def signup():
    register_fields = [
        "Mother's first name",
        "Father's first name",
        "BMI",
        "Number of EXs",
        "Number of Bar Soaps stuck\nin your mouth before",
        "Have you tried eating rubber ducks? If so, describe your experience",
        "Sometimes, life hits you hard.\nWhat motivated you to commit to act\nof terrorism using this client?",
        "Are you ready to fat shame\nyour coworker or family member?",
    ]
    layout_register = [
        [sg.Text("Sign Up / Register", font=(None, 20)), sg.Text("Make sure you read the Terms and Agreements and the"
                                                                 " Privacy Policy ;)")],
        [sg.Text("We require a lots of information in order for you to truly understand the potential of this client")],
        [sg.Text("Username"), sg.InputText(key="Username", do_not_clear=True)],
        [sg.Text("Host Server Address / Website Address"), sg.InputText(key="Address", do_not_clear=False)],
        [sg.Text("Password"), sg.InputText("", password_char="*", key="Password", do_not_clear=False)],
        [sg.Text("Confirm Password"), sg.InputText("", password_char="*", key="Confirm", do_not_clear=False)]
    ]
    from random import SystemRandom
    rand = SystemRandom()
    additionals = rand.choices(register_fields, k=rand.randint(25, 49))
    for i, x in enumerate(additionals):
        layout_register += [
            [sg.Text(text=str(bytes(x, encoding="UTF-8").decode(encoding="UTF-8"))), sg.Multiline(auto_size_text=True,
                                                                                                  autoscroll=True)]
        ]
    layout_register += [
        [sg.Button("Terms and Agreements"), sg.Button("Privacy Policy")],
        [sg.Checkbox("By marking this checkbox with a Verizon Wireless check mark that has a funky shape that is\n"
                     "somehow looking like a hockey stick, you agree to the aforementioned Terms and Agreements and\n"
                     "Privacy Policy and acknowledge and agree to everything I said before. If you simply didn't read\n"
                     "those terms and agreements or privacy policy, you'll wish you did and heeded my advice. Anyhow,\n"
                     "take care and enjoy, if you check the Verizon Wireless check-mark which has the odd formulaic\n"
                     "shape of a defunct cat.", default=False, key='Agreements')],
        [sg.Cancel(tooltip='Click to exit. Your data will be lost.'), sg.Submit(tooltip='Click to submit')],
        [sg.Text(text="Copyright 2019 YoomamaFTW", pad=(0, (((22.5 * len(additionals)) - 13.0357), 0)))]
    ]
    return layout_register


def initload():
    layout = [
        [sg.Text('Stay', font=(None, 20)), sg.Text('Hydrated', font=(None, 20))],
        [sg.Button("Login"), sg.Button("Log-In")],
        [sg.Button("Sign Up"), sg.Button("Register")],
        [sg.Exit(), sg.Button("About")]
    ]
    terms_agreements = 'You, the User, agree to the following terms and agreements:\n\n' \
                       '  1. Users on other parts of the network are allowed to terrorize you. ' \
                       'This includes but not limited to:\n\n' \
                       '     - Acts of destruction upon your computer (e.g. forced shutdowns, copying of files, ' \
                       'deletion of files, opening of malware/McAfee/Norton, opening ransomware, etc.)\n' \
                       '     - Acts of terrorism (e.g. 100s of notifications offloading on your computer, using up ' \
                       'all available RAM/memory, and killing your GPU because... why not?)\n' \
                       '  2. The Stay Hydrated Team is not responsible for damage to your computer. All code is open' \
                       'source and you should make sure to review the code for safety. Ths Stay Hydrated Team is NOT ' \
                       'legally bound to any destruction and is not legally responsible for any action that happens\n' \
                       '  3. You agree not to use our application for malicious purposes against users on a different' \
                       ' network. You agree to only use this application to target users within your dedicated server' \
                       ' or the dedicated server that someone else in your network has set up.\n' \
                       '  4. You agree to only write Python code to damage others within your own network. You also' \
                       ' agree that you allow others to target your computer, as well.' \
                       '\n\nYou have been warned.\n\n~Stay Hydrated Team\n\nApache 2.0 License can be found on ' \
                       'apache.org'
    privacy_policy = r'We do not actually collect any of your data. Your data stays within your home or workplace ' \
                     r"or server or WiFi network. It's practically useless for this application. However, it brings" \
                     r" me GREAT joy that you are actually reading legal parts! It really does cut down on time when " \
                     r"it comes to these registration forms; am I right? If you've gotten all the way down here, then" \
                     r" congrats! You don't actually have to fill in anything except for the username and password " \
                     "and password confirmation fields! I hope you have a wonderful day and a terrific experience " \
                     "with the Stay Hydrated Client\n\n~ Stay Hydrated Team"
    about_text = 'About Stay Hydrated\n\n' \
                 'Developed by blitzcraft, kyouma, Stoffel, and Yoom/YoomamaFTW, Stay Hydrated is a project developed' \
                 ' for the r/ProgrammerHumor hackathon with the theme of over-engineering.\n' \
                 "We want you to be able to stay healthy while using your computer! So there are great default check" \
                 "-ups that your employer or parent can deploy. For example, are your eyes far away from the screen?" \
                 "Have you taken a break from the screen? How much water have you drunk? Did you do your daily " \
                 "calisthenics? Most of these are already installed, but what's the point of checku-ups if there're " \
                 "no punishments?\n\n" \
                 "We got you covered! We will make sure there are effective punishments in place, " \
                 "such as forcefully shutting down a computer, opening 100 tabs full of cat videos, turn up your " \
                 "volume to 100%, and even call your mother telling her how fun you're having with this program. " \
                 "Additionally, other users within this network can join in on the punishing fun! They can program, in" \
                 " Python, some great punishments using the os module.\n\n" \
                 "The setup of this project is simple -- sorta simple: a server is setup on someone's computer, or" \
                 " a Raspberry Pi (hint hint), and the users download the client. The client will check on you with" \
                 "default health check-ups and custom inspections designed by fellow users. If a user fails his/her " \
                 "check-up, then other users are able to terrorize the failing user through tons of notifications, " \
                 'custom trolls, and custom "terrorist" attacks, which other users can create using Python. The ' \
                 'notifications can also be custom made by other users. All users must be connected to the same WiFi.'
    landing = sg.Window('Stay Hydrated', layout=layout, resizable=True)
    landing_active = True
    register_active = False
    login_active = False
    while True:
        ev1, val1 = landing.Read()
        if ev1 is None or ev1 == 'Exit':
            break
        elif ev1 == 'About':
            sg.PopupScrolled(about_text, title="Stay Hydrated | About")
        elif ev1 == 'Login' or ev1 == "Log-In":
            if not login_active and landing_active and not register_active:
                landing.Hide()
                login_active = True
                layout_login = [
                    [sg.Text("Login", font=(None, 20))],
                    [sg.Text("Username"), sg.InputText(key='Username')],
                    [sg.Text("Password"), sg.InputText("", password_char="*", key='Password')],
                    [sg.Submit(), sg.Exit(tooltip='Click to exit the login window. No data will be saved')]
                ]
                win_login = sg.Window(title="Stay Hydrated | Login", layout=layout_login)
                while True:
                    ev2, val2 = win_login.Read()
                    if ev2 is None or ev2 == 'Exit':
                        win_login.Close()
                        login_active = False
                        register_active = False
                        landing_active = True
                        landing.UnHide()
                        break
        elif ev1 == 'Sign Up' or ev1 == 'Register':
            if not register_active and not login_active and landing_active:
                landing.Hide()
                register_active = True
                win_register = sg.Window("Stay Hydrated | Register", resizable=True) \
                    .Layout([[sg.Column(layout=signup(), scrollable=True)]])
                while True:
                    ev3, val3 = win_register.Read()
                    if ev3 is None or ev3 == 'Exit' or ev3 == 'Cancel':
                        win_register.Close()
                        register_active = False
                        login_active = False
                        landing_active = True
                        landing.UnHide()
                        break
                    elif ev3 == 'Submit':
                        if val3['Agreements']:
                            if val3['Username'] is not None:
                                if val3["Address"] is not None:
                                    # send dummy request that returns "Valid"
                                    if val3['Password'] is not None:
                                        if val3['Confirm'] is not None:
                                            if val3['Password'] == val3['Confirm']:
                                                # send request using the requests package
                                                pass
                                            else:
                                                sg.Popup("Your passwords did not match. Reconfirm it.")
                                        else:
                                            sg.Popup("Please confirm your password.")
                                    else:
                                        sg.Popup("You need to fill out the password field.")
                                else:
                                    sg.Popup("You need to fill out the address to the server. It probably looks "
                                             "like this: 192.168.0.11")
                            else:
                                sg.Popup("Please provide a username. Make it count.")
                        else:
                            sg.Popup("You must agree to the Terms and Agreements and Privacy Policy by marking the box"
                                     " with a check-mark first.")
                    elif ev3 == 'Terms and Agreements':
                        sg.PopupScrolled(terms_agreements, title="Terms and Agreements")
                    elif ev3 == 'Privacy Policy':
                        sg.PopupScrolled(privacy_policy, title="Privacy Policy")
    landing.Close()


def mainload():
    layout = [
        [sg.Text(text="Here's the current location: ", key="_LINE1_")],
        [sg.OK()]
    ]
    win_main = sg.Window(title="Stay Hydrated | Register", layout=layout, resizable=True)
    while True:
        event, value = win_main.Read()


if __name__ == '__main__':
    initload()
    #mainload()

'''
pyinstaller --onefile -w --name=blah main.py
--name is the name of the file
-w leaves out terminal on startup of application
--onefile makes one file, namely. Unfortunately, it takes awhile to
    load everything. So TODO test if having several files is better than one
'''

'''
Cross-platform notifications: https://www.devdungeon.com/content/windows-desktop-notifications-python
https://github.com/kivy/plyer/blob/master/plyer/facades/notification.py
'''
