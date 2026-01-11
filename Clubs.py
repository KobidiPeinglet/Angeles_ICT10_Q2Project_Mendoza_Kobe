from pyscript import document, display

def Show_info(event=None):
    selected_club = document.getElementById("clubs").value
    output = document.getElementById("output")

#Clubs Information
    clubs = {
        "Club1" : {
            "name" : "Basketball Varsity",
            "description" : "Athletic fun to train your skill in Basketball",
            "location" : "Quadrangle",
            "time" : "2:30 - 3:30",
            "advisor" : "Mr. Layug",
            "number" : "24",
            "category" : "Sports"
        }, 
        "Club2" : {
            "name" : "ComArts",
            "description" : "The art of communicating, Learn how to step up your skills to speak",
            "location" : "Classroom",
            "time" : "2:30 - 3:30",
            "advisor" : "Mr. Alegrid",
            "number" : "20",
            "category" : "Communication"
        },
        "Club3" : {
            "name" : "Cocc",
            "description" : "Military training for students to train discipline and leadership and just pain and suffering",
            "location" : "Somewhere in school",
            "time" : "3:00 - 4:00",
            "advisor" : "Sir Santos",
            "number" : "21",
            "category" : "Military Training"
        },
        "Club4" : {
            "name" : "Glee Club",
            "description" : "A club full of Glee and singing, a place for your voice and show your talent",
            "location" : "5th floor Music Room",
            "time" : "2:30 - 3:30",
            "advisor" : "Ms. Aguirre",
            "number" : "29",
            "category" : "Singing"
        },
        "Club5" : {
            "name" : "Math Club",
            "description" : "More math to suffer by, Fun if you can actually understand it(Not really)",
            "location" : "A Classroom",
            "time" : "2:00 - 3:00",
            "advisor" : "Ms. Cristobal",
            "number" : "17",
            "category" : "Extra Curricular"
        },
        "Club6" : {
            "name" : "Robotics Club",
            "description" : "Scrapped Club, would've been fun for new engineers",
            "location" : "None",
            "time"  :"None",
            "advisor" : "Mr. Balajadia",
            "number" : "0",
            "category" : "Engineering"
        },
        "Club7" : {
            "name" : "Science Club",
            "description" :"Learn more Science and do expirements I think",
            "location" : "Science Lab",
            "time" : "2:30 - 3:30",
            "advisor" : "Ms. Galang",
            "number" : "18",
            "category" : "Extra Curricular"
        },
        "Club8" : {
            "name" : "Social Studies Club",
            "description" : "Study Socially, History, Philosophy, Debates, and stuff idk", 
            "location" : "Classroom",
            "time" : "2:00 - 3:00",
            "advisor" :"Mr. Roque",
            "number" : "16",
            "category" : "Extra Curricular"
        }
    }

    club = clubs.get(selected_club)

    if club:
        output.innerText = (
        f"{club['name']}\n"
        f"Description: {club['description']}\n"
        f"Location: {club['location']}\n"
        f"Meeting Time: {club['time']}\n"
        f"Advisor: {club['advisor']}\n"
        f"Number of Members: {club['number']}\n"
        f"Category: {club['category']}\n"
    )

    else:
        output.innerText = "No Club Information"