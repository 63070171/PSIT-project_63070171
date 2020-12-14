""" Probability Calculation Into Faculties's KMITL """
from receive_score import receive
def engineering(gat, pat1, pat3):
    """ Calculate Score For Engineering Faculty """
    score_gat = (gat / 300) * 20
    score_pat1 = (pat1 / 300) * 30
    score_pat3 = (pat3 / 300) * 50
    return score_gat + score_pat1 + score_pat3

def engineering_national(gat1, gat2, pat1, pat3):
    """ Calculate Score For Engineering Faculty National """
    score_gat1 = (gat1 / 150) * 10
    score_gat2 = (gat2 / 150) * 20
    score_pat1 = (pat1 / 300) * 30
    score_pat3 = (pat3 / 300) * 40
    return score_gat1 + score_gat2 + score_pat1 + score_pat3

def science(gat, pat1, pat2, branch):
    """ Calculate Score For Science Faculty """
    math_statistic_apply = lambda x, y: ((x / 300) * 20) + ((y / 300) * 80)
    science_computer = lambda x, y, z: ((x / 300) * 10) + ((y / 300) * 50) + ((z / 300) * 40)
    other_branch = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 30) + ((z / 300) * 50)

    if branch == "วิชาคณิตศาสตร์ประยุกต์" or branch == "วิชาสถิติประยุกต์":
        return math_statistic_apply(gat, pat1)
    elif branch == "วิชาวิทยาการคอมพิวเตอร์":
        return science_computer(gat, pat1, pat2)
    else:
        return other_branch(gat, pat1, pat2)

def architecture(gat, pat4, pat6, branch):
    """ Calculate Score For Architecture Faculty """
    main_architecture = lambda x, y: ((x / 300) * 30) + ((y / 300) * 70)
    architecture_3d = lambda x, y: ((x / 300) * 40) + ((y / 300) * 60)
    media_art = lambda x, y: ((x / 300) * 50) + ((y / 300) * 50)

    if branch == "วิชาสถาปัตยกรรมหลัก":
        return main_architecture(gat, pat4)
    elif branch == "วิชาการออกแบบสนเทศสามมิติและสื่อบูรณาการ":
        return architecture_3d(gat, pat4)
    else:
        return media_art(gat, pat6)

def business_administration(gat, pat1):
    """ Calculate Score For Business Administration Faculty """
    score_gat = (gat / 300) * 50
    score_pat1 = (pat1 / 300) * 50
    return score_gat + score_pat1

def information_technology(gat, pat1):
    """ Calculate Score For Information Technology Faculty """
    score_gat = (gat / 300) * 50
    score_pat1 = (pat1 / 300) * 50
    return score_gat + score_pat1

def food_industry(gat, pat1, pat2, branch):
    """ Calculate Score For Food Industry Faculty """
    food_sci = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 20) + ((z / 300) * 60)
    foodtransform = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 30) + ((z / 300) * 50)

    if branch in "วิชาวิทยาศาสตร์และเทคโนโลยีการอาหาร" or\
        branch == "วิชาเทคโนโลยีการหมักในอุตสาหกรรมอาหาร" or\
            branch == "วิชาวิทยาศาสตร์การประกอบอาหารและการจัดการการบริการอาหาร(หลักสูตรนานาชาติ)":
        return food_sci(gat, pat1, pat2)
    else:
        return foodtransform(gat, pat1, pat2)

def education_industry_technology(gat, pat2, pat3, pat4, pat5, branch):
    """ Calculate Score For Industrial Education and Technology Faculty """
    score = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 40) + ((z / 300) * 40)
    if branch == "สถาปัตยกรรม" or branch == "การออกแบบสิ่งแวดล้อมภายใน" or\
        branch == "ครุศาสตร์การออกแบบ":
        return score(gat, pat4, pat5)
    elif branch == "ครุศาสตร์วิศวกรรม":
        return score(gat, pat3, pat5)
    elif branch == "ครุศาสตร์เกษตร":
        return score(gat, pat2, pat5)

def agricultural_technology(gat85, pat1, pat2):
    """ Calculate Score For Agricultural Technology Faculty """
    score_gat85 = (gat85 / 150) * 20
    score_pat1 = (pat1 / 300) * 30
    score_pat2 = (pat2 / 300) * 50
    return score_gat85 + score_pat1 + score_pat2

def engineering_manufacturing(pat1, pat2, pat3):
    """ Calculate Score For Bachelor of Engineering Program in Manufacturing System Engineering """
    score = lambda x, y, z: ((x / 300) * 30) + ((y / 300) * 30) + ((z / 300) * 40)
    return score(pat1, pat2, pat3)

def bachelor_technokmitl(gat, pat1, pat2):
    """ Calculate Score For College of Nanotechnology KMITL """
    score = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 30) + ((z / 300) * 50)
    return score(gat, pat1, pat2)

def aviation_industry(gat, gat2, pat1, pat3, branch):
    """ Calculate Score For Aviation Industry KMITL """
    aviation = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 30) + ((z / 300) * 50)
    logistic = lambda x, y, z: ((x / 300) * 20) + ((y / 150) * 40) + ((z / 300) * 40)

    if branch == "วิชาวิศวกรรมการบินและนักบินพาณิชย์":
        return aviation(gat, pat1, pat2)
    else:
        return logistic(gat, gat2, pat1)

def imse(gat, pat1, pat3):
    """ Calculate Score For IMSE """
    score = lambda x, y, z: ((x / 300) * 20) + ((y / 300) * 30) + ((z / 300) * 50)
    return score(gat, pat1, pat2)

def kmitl_pcc(gat, pat1, pat2, pat3, faculty):
    """ Calculate Score For KMITL PCC """
    engineer = lambda x, y, z: ((x / 300) * 15) + ((y / 300) * 15) + ((z / 300) * 20)
    sci = lambda x, y, z: ((x / 300) * 10) + ((y / 300) * 10) + ((z / 300) * 30)
    agriculture = lambda x, y, z: ((x / 300) * 10) + ((y / 300) * 10) + ((z / 300) * 30)
    administration = lambda x, y: ((x / 300) * 30) + ((y / 300) * 20)

    if faculty == "วิศวกรรมศาสตร์วิทยาเขตชุมพรเขตรอุดมศักดิ์":
        return engineer(gat, pat1, pat3)
    elif faculty == "วิทยาศาสตร์วิทยาเขตชุมพรเขตรอุดมศักดิ์":
        return sci(gat, pat1, pat2)
    elif faculty == "เทคโนโลยีการเกษตรวิทยาเขตชุมพรเขตรอุดมศักดิ์":
        return agriculture(gat, pat1, pat2)
    else:
        return administration(gat, pat1)
