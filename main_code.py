import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 

dict_emails = {"email1":"lastname1", "email2":"lastname2"} #modify so it contains the professors' emails and last names

fromaddr = "you@gmail.com" #your email
for i in dict_emails:
    toaddr = i
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Summer Internship"
    
    #modify the body below as you wish
    body = """
    Hello Professor %s:

    My name is [...], and I am a sophomore at [...] High School in [...]. I am wondering if you would consider offering me a summer internship with you to do research and ultimately expand my knowledge in science, technology, engineering, and mathematics.

    For some background information, I am intrigued by STEM and have pursued this passion in high school through competitions. For starters, I am part of a model rocketry team for the Team America Rocketry Challenge, America's largest rocketry competition. By being part of this team, I have gotten exposure to a variety of aerospace and physics concepts, as well as developing useful skills such as creative problem solving and thinking on the spot. In this team recently, a significant portion of our time has been dedicated to working with Arduino Uno, a microcontroller which we use to adjust the shroud length of our parachute and ultimately gain control of our rocket's descent time. In the summer, I hope to expand my knowledge on Arduino and eventually share my passion about this by forming a club in my school junior year. Now we have come far, as through our hard work and dedication we have gained points that almost guarantees our spot to compete with the top 100 teams in finals this May. Our website highlights our achievements.

    Along with TARC rocketry, I am in my school's Odyssey of the Mind Club, which participates in the annual TEAMS competition. This year in the [...] contest, our school's 9/10 team placed 3rd in [...], and hopefully our points were high enough for us to compete in the national level this summer. Odyssey of the Mind has also introduced me to VEX robotics, where we will be competing in April 16 at the regional level. I also pursue STEM through technical theater, where I have been in the carpentry crew for four shows and have thus learned a lot about precision and efficiency. As for computer science, I have taken courses in Python and know some C programming due to my experience in Arduino. Finally, math has always been my favorite subject, as I excel in it more than any of the others. In school I am in honors pre-calculus right now and am self studying AP Calculus, and most of the letters of recommendations I get are from math as I avidly participate in that class the most. My achievements include qualifying for the AIME, but my attention has been turned to USAMO, and I can see it is a feasible goal for next year as I am at a 7 level right now for the AIME.

    Now, I know all these STEM extracurriculars may not apply to you, but I have included these not to brag but to demonstrate my passion for STEM and my work ethics. I assure you that I will work hard if you allow me to be your intern; in fact, I have worked 12 hours a day in the past for technical theater, so I will not fail in terms of commitment. I know you have a busy life, but PLEASE consider me to become an intern for you in the summer.

    Thank you,

    [...]
    """ %dict_emails[i]

    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "psswd") #modify your password
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
server.quit()
