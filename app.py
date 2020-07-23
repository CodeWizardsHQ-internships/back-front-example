from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config["DEBUG"] = True

text_field_value_back_end = "initial text"  #defining a global var with the initial text


# ---- ROUTES ----

@app.route('/', methods=['GET', 'POST'])
def home():
    global text_field_value_back_end

    if request.method == 'POST':
        button_clicked = request.form['action']
        if button_clicked == 'update':
            input_text = request.form['current_text']
            text_field_value_back_end = update_text(input_text)
        elif button_clicked == 'delete':
            text_field_value_back_end = delete_text()
        elif button_clicked == 'reset':
            text_field_value_back_end = reset_text()
            

    return render_template('example.html', text_field_value = text_field_value_back_end)

    

# ---- FUNCTIONS ----    

def update_text(input):
    #you could interact with a database here
    return input

def delete_text():
    #you could interact with a database here
    return ""

def reset_text():
    #you could interact with a database here
    return "initial text"
