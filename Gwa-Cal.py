from pyscript import document, display

def calculate(event=None):
    try:
        #Get input values
        Sub1 = float(document.getElementById("Math").value or 0)
        Sub2 = float(document.getElementById("Science").value or 0)
        Sub3 = float(document.getElementById("Fil").value or 0)
        Sub4 = float(document.getElementById("Eng").value or 0)
        Sub5 = float(document.getElementById("PE").value or 0)
        Sub6 = float(document.getElementById("ICT").value or 0)

        #Get the general weighted average
        GWA = (Sub1 + Sub2 + Sub3 + Sub4 + Sub5 + Sub6) / 6

        #Student Details
        Fname = document.getElementById("Fname").value
        Lname = document.getElementById("Lname").value
        GandS = document.getElementById("G_S").value

        #output in index
        output_text = f"""
            Name: {Fname} {Lname}
            Grade and Section: {GandS}
            Math: {Sub1}
            Science: {Sub2}
            Filipino: {Sub3}
            English: {Sub4}
            PE: {Sub5}
            ICT: {Sub6}
            The General Weighted Average: {GWA:.2f}
            """

        # Display in the output div
        document.getElementById("output").innerText = output_text

    except ValueError:
        display("Please enter valid numbers for all grades.", target="output")