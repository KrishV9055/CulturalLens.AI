import numpy as np
from PIL import Image
import tensorflow as tf
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template
import os

city_coordinates = {
    'Jantar_Mantar': {'city': 'Jaipur', 'coordinates': [26.9260, 75.8238]},
    'Ajmer_Shareef': {'city': 'Ajmer', 'coordinates': [26.4499, 74.6399]},
    'Ranakpur_Temple': {'city': 'Ranakpur', 'coordinates': [25.1228, 73.4330]},
    'Meenakshi_Amman_Temple': {'city': 'Madurai', 'coordinates': [9.9195, 78.1190]},
    'Hampi_Ruins': {'city': 'Hampi', 'coordinates': [15.3350, 76.4600]},
    'Jaisalmer_Fort': {'city': 'Jaisalmer', 'coordinates': [26.9124, 70.9127]},
    'Sanchi_Stupa': {'city': 'Sanchi', 'coordinates': [23.4821, 77.7383]},
    'Mahabalipuram_Shore_Temple': {'city': 'Mahabalipuram', 'coordinates': [12.6269, 80.1713]},
    'Rashtrapati_Bhavan': {'city': 'Delhi', 'coordinates': [28.6145, 77.1996]},
    'Ajmer_Fort': {'city': 'Ajmer', 'coordinates': [26.4499, 74.6399]},
    'Amer_Fort': {'city': 'Jaipur', 'coordinates': [26.9855, 75.8513]},
    'Sundarbans': {'city': 'Sundarbans', 'coordinates': [21.9475, 88.9458]},
    'Daulatabad_Fort': {'city': 'Aurangabad', 'coordinates': [19.9369, 75.2353]},
    'Rann_of_Kutch': {'city': 'Kutch', 'coordinates': [23.7337, 69.8597]},
    'Gwalior_Fort': {'city': 'Gwalior', 'coordinates': [26.2303, 78.1689]},
    'Sanchi_Stupa': {'city': 'Sanchi', 'coordinates': [23.4821, 77.7383]},
    'Ajanta_Caves': {'city': 'Aurangabad', 'coordinates': [20.5514, 75.7037]},
    'Kumbhalgarh_Fort': {'city': 'Kumbhalgarh', 'coordinates': [25.1489, 73.5877]},
    'Mehrangarh_Fort': {'city': 'Jodhpur', 'coordinates': [26.2981, 73.0182]},
    'Halebidu_Temple': {'city': 'Halebidu', 'coordinates': [13.2072, 75.9906]},
    'Bodh_Gaya': {'city': 'Gaya', 'coordinates': [24.6955, 84.9877]},
    'Ajanta_Caves': {'city': 'Aurangabad', 'coordinates': [19.8776, 75.3423]},
    'Charar-e-Sharief_shrine': {'city': 'Srinagar', 'coordinates': [34.0836, 74.7973]},
    'Chota_Imambara': {'city': 'Lucknow', 'coordinates': [26.8467, 80.9462]},
    'Ellora_Caves': {'city': 'Aurangabad', 'coordinates': [20.0262, 75.1833]},
    'Fatehpur_Sikri': {'city': 'Fatehpur Sikri', 'coordinates': [27.0947, 77.6677]},
    'Gateway_of_India': {'city': 'Mumbai', 'coordinates': [18.9217, 72.8342]},
    'Hawa_Mahal': {'city': 'Jaipur', 'coordinates': [26.9239, 75.8265]},
    'Humayun%27s_Tomb': {'city': 'Delhi', 'coordinates': [28.5933, 77.2507]},
    'India_Gate': {'city': 'Delhi', 'coordinates': [28.6129, 77.2295]},
    'Khajuraho': {'city': 'Khajuraho', 'coordinates': [24.8318, 79.9226]},
    'Konark_Sun_Temple': {'city': 'Konark', 'coordinates': [19.8762, 86.0925]},
    'Alai_Darwaza': {'city': 'Delhi', 'coordinates': [28.6149, 77.2344]},
    'Alai_Minar': {'city': 'Delhi', 'coordinates': [28.6135, 77.1987]},
    'Basilica_of_Bom_Jesus': {'city': 'Goa', 'coordinates': [15.5007, 73.9155]},
    'Charminar': {'city': 'Hyderabad', 'coordinates': [17.3616, 78.4747]},
    'Golden_Temple': {'city': 'Amritsar', 'coordinates': [31.6204, 75.3815]},
    'Iron_pillar_of_Delhi': {'city': 'Delhi', 'coordinates': [28.5245, 77.1855]},
    'Jamali_Kamali_Mosque_and_Tomb': {'city': 'Delhi', 'coordinates': [28.5275, 77.1785]},
    'Lotus_Temple': {'city': 'Delhi', 'coordinates': [28.5535, 77.2588]},
    'Mysore_Palace': {'city': 'Mysuru', 'coordinates': [12.3051, 76.6551]},
    'Qutb_Minar': {'city': 'Delhi', 'coordinates': [28.5244, 77.1855]},
    'Taj_Mahal': {'city': 'Agra', 'coordinates': [27.1751, 78.0421]},
    'Brihadisvara_Temple': {'city': 'Thanjavur', 'coordinates': [10.7805, 79.1311]},
    'Victoria_Memorial,_Kolkata': {'city': 'Kolkata', 'coordinates': [22.5455, 88.3420]},
        # Aurangabad
    'Bibi_Ka_Maqbara': {'city': 'Aurangabad', 'coordinates': [19.9195, 75.3580]},
    'Aurangabad_Caves': {'city': 'Aurangabad', 'coordinates': [20.0107, 75.6754]},
    'Panchakki': {'city': 'Aurangabad', 'coordinates': [19.9016, 75.3176]},
    'Daulatabad_Fort_2': {'city': 'Aurangabad', 'coordinates': [19.9459, 75.2511]},
    'Grishneshwar_Jyotirlinga': {'city': 'Aurangabad', 'coordinates': [20.0262, 75.1874]},
    'Khuldabad': {'city': 'Aurangabad', 'coordinates': [20.0434, 75.3963]},
    'Aurangzeb\'s_Tomb': {'city': 'Aurangabad', 'coordinates': [19.8946, 75.3496]},
    'Siddharth_Garden_and_Zoo': {'city': 'Aurangabad', 'coordinates': [19.8734, 75.3667]},
    'Salim_Ali_Lake': {'city': 'Aurangabad', 'coordinates': [19.8968, 75.3245]},
    'Gautala_Wildlife_Sanctuary': {'city': 'Aurangabad', 'coordinates': [19.7842, 75.3401]},

    # Srinagar
    'Shalimar_Bagh': {'city': 'Srinagar', 'coordinates': [34.1083, 74.8003]},
    'Nishat_Bagh': {'city': 'Srinagar', 'coordinates': [34.0976, 74.8030]},
    'Jamia_Masjid': {'city': 'Srinagar', 'coordinates': [34.0926, 74.7982]},
    'Chashme_Shahi': {'city': 'Srinagar', 'coordinates': [34.1176, 74.8284]},
    'Shankaracharya_Temple': {'city': 'Srinagar', 'coordinates': [34.0917, 74.7913]},
    'Hazratbal_Shrine': {'city': 'Srinagar', 'coordinates': [34.0983, 74.8007]},
    'Pari_Mahal': {'city': 'Srinagar', 'coordinates': [34.0863, 74.8415]},
    'Dal_Lake': {'city': 'Srinagar', 'coordinates': [34.0837, 74.7976]},
    'Shikara_Ride': {'city': 'Srinagar', 'coordinates': [34.0832, 74.8069]},
    'Jama_Masjid_Srinagar': {'city': 'Srinagar', 'coordinates': [34.0898, 74.7973]},

    # Lucknow
    'Bara_Imambara': {'city': 'Lucknow', 'coordinates': [26.8745, 80.9341]},
    'Chattar_ManZil': {'city': 'Lucknow', 'coordinates': [26.8554, 80.9423]},
    'Rumi_Darwaza': {'city': 'Lucknow', 'coordinates': [26.8739, 80.9341]},
    'British_Residency': {'city': 'Lucknow', 'coordinates': [26.8623, 80.9493]},
    'Hazratganj': {'city': 'Lucknow', 'coordinates': [26.8533, 80.9387]},
    'Janeshwar_Mishra_Park': {'city': 'Lucknow', 'coordinates': [26.8236, 81.0056]},
    'Ambedkar_Park': {'city': 'Lucknow', 'coordinates': [26.8872, 80.9792]},
    'Lucknow_Zoo': {'city': 'Lucknow', 'coordinates': [26.8535, 80.9471]},
    'Bara_Imambara_Rumi_Darwaza_Night': {'city': 'Lucknow', 'coordinates': [26.8745, 80.9341]},
    'Gomti_Riverfront': {'city': 'Lucknow', 'coordinates': [26.8391, 80.9422]},
    
    # Delhi
    'Jama_Masjid': {'city': 'Delhi', 'coordinates': [28.6507, 77.2334]},
    'Red_Fort': {'city': 'Delhi', 'coordinates': [28.6562, 77.2410]},
    'India_Habitat_Centre': {'city': 'Delhi', 'coordinates': [28.5848, 77.2271]},
    'Agrasen_ki_Baoli': {'city': 'Delhi', 'coordinates': [28.6261, 77.2262]},
    'National_Zoological_Park': {'city': 'Delhi', 'coordinates': [28.6090, 77.2439]},
    'Lotus_Temple_Night': {'city': 'Delhi', 'coordinates': [28.5535, 77.2588]},
    'National_Museum': {'city': 'Delhi', 'coordinates': [28.6119, 77.2194]},
    'Akshardham_Temple': {'city': 'Delhi', 'coordinates': [28.6127, 77.2773]},
    'Connaught_Place': {'city': 'Delhi', 'coordinates': [28.6315, 77.2167]},
    'Jantar_Mantar_2': {'city': 'Delhi', 'coordinates': [28.6271, 77.2166]},

    # Mumbai
    'Gateway_of_India_2': {'city': 'Mumbai', 'coordinates': [18.9223, 72.8347]},
    'Chhatrapati_Shivaji_Terminus': {'city': 'Mumbai', 'coordinates': [18.9401, 72.8354]},
    'Elephanta_Caves': {'city': 'Mumbai', 'coordinates': [18.9647, 72.9302]},
    'Marine_Drive': {'city': 'Mumbai', 'coordinates': [18.9438, 72.8247]},
    'Siddhivinayak_Temple': {'city': 'Mumbai', 'coordinates': [19.0273, 72.8532]},
    'Haji_Ali_Dargah': {'city': 'Mumbai', 'coordinates': [18.9829, 72.8106]},
    'Kanheri_Caves': {'city': 'Mumbai', 'coordinates': [19.2156, 72.9097]},
    'Sanjay_Gandhi_National_Park': {'city': 'Mumbai', 'coordinates': [19.2141, 72.9100]},
    'Juhu_Beach': {'city': 'Mumbai', 'coordinates': [19.0880, 72.8265]},
    'Mumbai_Skyline': {'city': 'Mumbai', 'coordinates': [19.0760, 72.8777]},

    # Jaipur
    'City_Palace': {'city': 'Jaipur', 'coordinates': [26.9256, 75.8236]},
    'Hawa_Mahal_2': {'city': 'Jaipur', 'coordinates': [26.9239, 75.8265]},
    'Jal_Mahal': {'city': 'Jaipur', 'coordinates': [26.9532, 75.8550]},
    'Albert_Hall_Museum': {'city': 'Jaipur', 'coordinates': [26.9124, 75.7873]},
    'Jaigarh_Fort': {'city': 'Jaipur', 'coordinates': [26.9855, 75.8493]},
    'Nahargarh_Fort': {'city': 'Jaipur', 'coordinates': [26.9484, 75.8007]},
    'Rambagh_Palace': {'city': 'Jaipur', 'coordinates': [26.8882, 75.8087]},
    'Amber_Fort': {'city': 'Jaipur', 'coordinates': [26.9855, 75.8513]},
    'Sisodia_Rani_Ka_Bagh': {'city': 'Jaipur', 'coordinates': [26.8866, 75.7736]},
    'Jaipur_Zoo': {'city': 'Jaipur', 'coordinates': [26.9004, 75.8117]},

    'Panch_Mahal': {'city': 'Fatehpur Sikri', 'coordinates': [27.0941, 77.6675]},
    'Buland_Darwaza': {'city': 'Fatehpur Sikri', 'coordinates': [27.0943, 77.6607]},
    'Diwan-i-Khas': {'city': 'Fatehpur Sikri', 'coordinates': [27.0947, 77.6653]},
    'Hiran_Minar': {'city': 'Fatehpur Sikri', 'coordinates': [27.0918, 77.6707]},
    'Jama_Masjid_Fatehpur_Sikri': {'city': 'Fatehpur Sikri', 'coordinates': [27.0920, 77.6689]},
    'Fatehpur_Sikri_2': {'city': 'Fatehpur Sikri', 'coordinates': [27.0942, 77.6680]},
    'Fatehpur_Sikri_Night': {'city': 'Fatehpur Sikri', 'coordinates': [27.0937, 77.6687]},
    'Salim_Chishti_Mosque': {'city': 'Fatehpur Sikri', 'coordinates': [27.0930, 77.6693]},
    'Diwan-i-Am': {'city': 'Fatehpur Sikri', 'coordinates': [27.0949, 77.6667]},
    'Fatehpur_Sikri_3': {'city': 'Fatehpur Sikri', 'coordinates': [27.0925, 77.6670]},

    # Additional Monuments for Khajuraho
    'Kandariya_Mahadeva_Temple': {'city': 'Khajuraho', 'coordinates': [24.8313, 79.9311]},
    'Duladeo_Temple': {'city': 'Khajuraho', 'coordinates': [24.8447, 79.9342]},
    'Lakshmana_Temple': {'city': 'Khajuraho', 'coordinates': [24.8327, 79.9332]},
    'Vishwanath_Temple_Khajuraho': {'city': 'Khajuraho', 'coordinates': [24.8343, 79.9336]},
    'Chaturbhuj_Temple': {'city': 'Khajuraho', 'coordinates': [24.8345, 79.9318]},
    'Parshvanatha_Temple': {'city': 'Khajuraho', 'coordinates': [24.8316, 79.9312]},
    'Adinatha_Temple': {'city': 'Khajuraho', 'coordinates': [24.8329, 79.9305]},
    'Khajuraho_Western_Group_of_Temples': {'city': 'Khajuraho', 'coordinates': [24.8342, 79.9274]},
    'Vamana_Temple': {'city': 'Khajuraho', 'coordinates': [24.8340, 79.9298]},
    'Devi_Jagadambi_Temple': {'city': 'Khajuraho', 'coordinates': [24.8317, 79.9331]},

    # Additional Monuments for Goa
    'Sequa': {'city': 'Goa', 'coordinates': [15.2946, 74.1240]},
    'Basilica_of_Bom_Jesus_2': {'city': 'Goa', 'coordinates': [15.5005, 73.9111]},
    'Fort_Aguada': {'city': 'Goa', 'coordinates': [15.4982, 73.7491]},
    'Salim_Ali_Bird_Sanctuary': {'city': 'Goa', 'coordinates': [15.4215, 73.9436]},
    'Chapora_Fort': {'city': 'Goa', 'coordinates': [15.6035, 73.7398]},
    'Dudhsagar_Waterfalls': {'city': 'Goa', 'coordinates': [15.3140, 74.3146]},
    'Mangueshi_Temple': {'city': 'Goa', 'coordinates': [15.4083, 74.0035]},
    'Anjuna_Beach': {'city': 'Goa', 'coordinates': [15.5513, 73.7462]},
    'Colva_Beach': {'city': 'Goa', 'coordinates': [15.2687, 73.9200]},
    'Shantadurga_Temple': {'city': 'Goa', 'coordinates': [15.4228, 74.0057]},

    # Additional Monuments for Konark
    'Sun_Temple_Konark_2': {'city': 'Konark', 'coordinates': [19.8759, 86.0922]},
    'Chandrabhaga_Beach': {'city': 'Konark', 'coordinates': [19.8540, 86.0946]},
    'Ramachandi_Temple': {'city': 'Konark', 'coordinates': [19.8311, 86.0734]},
    'Kakatpur_Mangala_Temple': {'city': 'Konark', 'coordinates': [19.9689, 86.0607]},
    'Astranga': {'city': 'Konark', 'coordinates': [19.8051, 86.1290]},
    'Konark_Nautical_Archaeology_Museum': {'city': 'Konark', 'coordinates': [19.8900, 86.0966]},
    'Baleshwar_Beach': {'city': 'Konark', 'coordinates': [19.8303, 86.1271]},
    'Raghurajpur': {'city': 'Konark', 'coordinates': [19.9979, 86.0890]},
    'Ashokan_Edicts_Rock_Edicts_of_Dhauli': {'city': 'Konark', 'coordinates': [20.1883, 85.8406]},
    'Baliharachandi_Beach': {'city': 'Konark', 'coordinates': [19.8941, 86.0883]},

    # Additional Monuments for Amritsar
    'Akal_Takht': {'city': 'Amritsar', 'coordinates': [31.6186, 74.8743]},
    'Jallianwala_Bagh': {'city': 'Amritsar', 'coordinates': [31.6230, 74.8741]},
    'Maharaja_Ranjit_Singh_Museum': {'city': 'Amritsar', 'coordinates': [31.6228, 74.8747]},
    'Rambagh_Gardens': {'city': 'Amritsar', 'coordinates': [31.6260, 74.8804]},
    'Durgiana_Temple': {'city': 'Amritsar', 'coordinates': [31.6304, 74.8756]},
    'Partition_Museum': {'city': 'Amritsar', 'coordinates': [31.6305, 74.8765]},
    'Taran_Taran_Sahib': {'city': 'Amritsar', 'coordinates': [31.4466, 74.9250]},
    'Maharaja_Ranjit_Singh_Panjabi_Museum': {'city': 'Amritsar', 'coordinates': [31.6192, 74.8764]},
    'Gobindgarh_Fort': {'city': 'Amritsar', 'coordinates': [31.6190, 74.8760]},
    'Partition_Gallery': {'city': 'Amritsar', 'coordinates': [31.6194, 74.8752]},
    
    }

app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER = 'D://Advance Python Project//website//uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monuments_identification', methods=['POST'])



def monuments_identification():
    print("Python code reached")
    if 'image' not in request.files:
        return "No image file provided", 400

    image_file = request.files['image']
    if image_file.filename == '':
        return "No selected image file", 400

    try:
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(image_path)

        # Loading model 
        loaded_model = tf.keras.models.load_model("D://Advance Python Project//website//updated_model.h5")

        # Declaring label_map
        label_map = {'Ajanta_Caves': 0, 'Charar-e-Sharief_shrine': 1, 'Chota_Imambara': 2, 'Ellora_Caves': 3, 'Fatehpur_Sikri': 4, 'Gateway_of_India': 5, 'Humayun%27s_Tomb': 6, 'India_Gate': 7, 'Khajuraho': 8, 'Konark_Sun_Temple': 9, 'Alai_Darwaza': 10, 'Alai_Minar': 11, 'Basilica_of_Bom_Jesus': 12, 'Charminar': 13, 'Golden_Temple': 14, 'Hawa_Mahal': 15, 'Iron_pillar_of_Delhi': 16, 'Jamali_Kamali_Mosque_and_Tomb': 17, 'Lotus_Temple': 18, 'Mysore_Palace': 19, 'Qutb_Minar': 20, 'Taj_Mahal': 21, 'Brihadisvara_Temple': 22, 'Victoria_Memorial,_Kolkata':23}
        
        # Function to predict and get monument name
        def prediction(image_path, model):
            img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
            x = tf.keras.preprocessing.image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
            preds = model.predict(x)
            predicted_class = np.argmax(preds)
            monument_name = list(label_map.keys())[predicted_class]
            print('confidence score of: ', np.max(preds))
            return monument_name, predicted_class

        # Get monument name and class
        monument_name, predicted_class = prediction(image_path, loaded_model)
        city, coordinates = get_city_and_coordinates(monument_name)
        other_monuments = []
        for monument, info in city_coordinates.items():
            if info['city'] == city and monument != monument_name:
                other_monuments.append({'name': monument, 'coordinates': info['coordinates']})
        return render_template('index.html', monument_name=monument_name,monument_coordinates=coordinates, city=city, other_monuments=other_monuments)


    except Exception as e:
        return str(e), 500

def get_monument_coordinates(monument_class):
    # Coordinates for each monument (replace with actual coordinates)
    coordinates = {
        0: [10.5528, 30.7037],   # Ajanta Caves
        1: [34.2016, 74.3639],   # Charar-E- Sharif
        2: [26.8393, 80.9361],   # Chhota Imambara
        3: [20.0262, 75.1833],   # Ellora Caves
        4: [27.0947, 77.6677],   # Fatehpur Sikri
        5: [18.9217, 72.8342],   # Gateway of India
        6: [26.9239, 75.8265],   # Hawa Mahal
        7: [28.5933, 77.2507],   # Humayun's Tomb
        8: [28.6129, 77.2295],   # India Gate
        9: [24.8318, 79.9226],   # Khajuraho
        10: [19.8762, 86.0925],  # Sun Temple Konark
        11: [28.6149, 77.2344],  # Alai Darwaza
        12: [28.6135, 77.1987],  # Alai Minar
        13: [15.5007, 73.9155],  # Basilica of Bom Jesus
        14: [17.3616, 78.4747],  # Charminar
        15: [31.6204, 75.3815],  # Golden Temple
        16: [28.5245, 77.1855],  # Iron Pillar
        17: [28.5275, 77.1785],  # Jamali Kamali Tomb
        18: [28.5535, 77.2588],  # Lotus Temple
        19: [12.3051, 76.6551],  # Mysore Palace
        20: [28.5244, 77.1855],  # Qutub Minar
        21: [27.1751, 78.0421],  # Taj Mahal
        22: [10.7805, 79.1311],  # Tanjavur Temple
        23: [22.5455, 88.3420]   # Victoria Memorial
    }
    return coordinates.get(monument_class, [0, 0])  # Default to [0, 0] if coordinates are not available

def get_city_and_coordinates(monument_class):
    monument_info = city_coordinates.get(monument_class, {'city': 'Unknown', 'coordinates': [0, 0]})
    return monument_info['city'], monument_info['coordinates']

if __name__ == '__main__':
    app.run(debug=True)