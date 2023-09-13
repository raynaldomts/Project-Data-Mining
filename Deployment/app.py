from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model_fraud.sav', 'rb')
model = pickle.load(model_file, encoding='bytes')
#add
@app.route('/')
def index():
    return render_template('index.html', insurance_cost=" ")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    typeppk, cmg_type,diagprimer_type,umur,los_type, kdkc ,jkpst, jnspelsep,severity= [x for x in request.form.values()]

    data = []

    
    if typeppk == 'A':
        data.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'B':
        data.extend([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'C':
        data.extend([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'D':
        data.extend([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'GD':
        data.extend([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'HD':
        data.extend([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'I1':
        data.extend([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'I2':
        data.extend([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'I3':
        data.extend([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'I4':
        data.extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KB':
        data.extend([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KC':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KG':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KI':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])     
    elif  typeppk == 'KJ':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KL':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KM':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
    elif  typeppk == 'KO':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
    elif  typeppk == 'KP':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
    elif  typeppk == 'KT':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
    elif  typeppk == 'KU':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
    elif  typeppk == 'SA':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    elif  typeppk == 'SB':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
    elif  typeppk == 'SC':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
    elif  typeppk == 'SD':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

    if cmg_type == 'A':
        data.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'B':
        data.extend([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'C':
        data.extend([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'D':
        data.extend([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])            
    elif cmg_type == 'E':
        data.extend([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'F':
        data.extend([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])   
    elif cmg_type == 'G':
        data.extend([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'H':
        data.extend([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'I':
        data.extend([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])            
    elif cmg_type == 'J':
        data.extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'K':
        data.extend([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]) 
    elif cmg_type == 'L':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'M':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
    elif cmg_type == 'N':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])            
    elif cmg_type == 'O':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
    elif cmg_type == 'P':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]) 
    elif cmg_type == 'Q':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
    elif cmg_type == 'S':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])            
    elif cmg_type == 'T':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])  
    elif cmg_type == 'U':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]) 
    elif cmg_type == 'V':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])          
    elif cmg_type == 'W':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])  
    elif cmg_type == 'Z':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]) 
    
    if diagprimer_type == 'diagprimer_a00_b99':
        data.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_c00_d48':
        data.extend([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_d50_d89':
        data.extend([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_e00_e90':
        data.extend([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_f00_f99':
        data.extend([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_g00_g99':
        data.extend([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_h00_h59':
        data.extend([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_h60_h95':
        data.extend([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_i00_i99':
        data.extend([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_j00_j99':
        data.extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_k00_k93':
        data.extend([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_l00_l99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_m00_m99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_n00_n99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_o00_o99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_p00_p96':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
    elif diagprimer_type == 'diagprimer_q00_q99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
    elif diagprimer_type == 'diagprimer_r00_r99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    elif diagprimer_type == 'diagprimer_s00_s98':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
    elif diagprimer_type == 'diagprimer_u00_u85':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
    elif diagprimer_type == 'diagprimer_z00_z99':
        data.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

    
    if umur == 'satu':
        data.extend([1, 0, 0, 0, 0])
    elif umur == 'dua':
        data.extend([0, 1, 0, 0, 0])
    elif umur == 'tiga':
        data.extend([0,0, 1, 0, 0])
    elif umur == 'empat':
        data.extend([0,0, 0, 1, 0])
    elif umur == 'lima':
        data.extend([0,0, 0, 0, 1])
    
    if los_type == 'los_rawat_jalan':
        data.extend([1,0,0,0])
    elif los_type == 'los_short_stay':
        data.extend([0,1,0,0])
    elif los_type == 'los_long_stay':
        data.extend([0,0,1,0])
    elif los_type == 'los_long_stay':
        data.extend([0,0,0,1])
    
    data.extend([int(kdkc)])

    if jkpst == '0':
        data.extend([0])
    else :
        data.extend([1])
    
    if jnspelsep == '1':
        data.extend([1])
    else :
        data.extend([2])

    if severity == '0':
        data.extend([0])
    elif severity == '1':
        data.extend([1])
    elif severity == '2':
        data.extend([2])
    elif severity == '3':
        data.extend([3])


    prediction = model.predict([data])
    output = round(prediction[0], 2)
    message =''
    if (output == 0):
        message = "not fraud"
    else:
        message = "fraud"

    return render_template('index.html', insurance_cost=message)


if __name__ == '__main__':
    app.run(debug=True)