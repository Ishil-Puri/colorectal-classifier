from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)  # Handle CORS if accessing from different origins
print("tf_version: " + tf.__version__)
model = tf.keras.models.load_model('./colo_model2.h5')

class_names = {0: 'tumour epithelium', 1: 'simple stroma',
            2: 'complex stroma', 3: 'immune cell conglomerates',
            4: 'debris and mucus', 5: 'mucosal glands',
            6: 'adipose tissue', 7: 'background'}

calibration_nonconformity_scores = np.array([7.77213573e-02, 1.71021283e-01, 6.51900291e-01, 3.00793052e-01,
       2.05327272e-01, 3.85159254e-02, 4.38719928e-01, 1.18654191e-01,
       6.57408595e-01, 7.94509530e-01, 3.05062532e-02, 7.26040006e-02,
       1.49908721e-01, 8.25978518e-02, 1.35008514e-01, 2.33982205e-02,
       9.16144609e-01, 4.54566419e-01, 8.19487572e-02, 1.76783442e-01,
       8.79819512e-01, 4.10223782e-01, 7.67364562e-01, 2.83082724e-02,
       5.60257673e-01, 3.63329053e-01, 6.93828464e-02, 5.72585523e-01,
       7.62021542e-02, 1.94387138e-01, 9.85418022e-01, 7.98689127e-02,
       1.66480243e-01, 7.14804351e-01, 4.32503223e-03, 1.56111717e-02,
       3.24072540e-01, 1.97858274e-01, 3.92502964e-01, 7.25732267e-01,
       6.04302645e-01, 2.63428688e-01, 5.01604319e-01, 2.05934048e-02,
       3.68336499e-01, 6.41518831e-02, 7.75408149e-02, 2.10846066e-02,
       9.29108679e-01, 7.72139430e-02, 7.72656798e-02, 1.22589231e-01,
       4.19728696e-01, 2.49128342e-02, 5.66303134e-01, 6.32024348e-01,
       2.27826834e-02, 4.27817523e-01, 3.79348993e-01, 6.60557151e-02,
       7.31080770e-01, 9.32197511e-01, 9.20354784e-01, 7.34974742e-02,
       6.36132061e-01, 7.83942938e-02, 7.72533417e-02, 1.80048287e-01,
       1.00488484e-01, 5.76217771e-02, 8.46301079e-01, 7.46852994e-01,
       2.74962485e-01, 2.58349538e-01, 9.88509059e-02, 7.68191218e-02,
       6.20171368e-01, 8.23270082e-02, 2.81560421e-03, 2.86862850e-02,
       1.76749885e-01, 8.46048057e-01, 3.87234688e-02, 9.35403883e-01,
       1.96152925e-01, 2.20424235e-01, 7.84990191e-02, 4.63833213e-02,
       3.94756019e-01, 5.40963888e-01, 7.25619793e-02, 5.30915439e-01,
       7.61390328e-02, 2.48690963e-01, 1.76627696e-01, 6.88202918e-01,
       5.01969457e-01, 2.81077325e-01, 1.26795769e-02, 2.39748597e-01,
       7.52018094e-02, 5.73058605e-01, 8.45683336e-01, 9.63729560e-01,
       2.23202229e-01, 1.35763288e-01, 7.04727769e-02, 2.31155992e-01,
       4.43250895e-01, 2.06089616e-02, 4.10008430e-03, 1.46362066e-01,
       3.09705734e-03, 2.55727530e-01, 2.14889646e-02, 3.90321434e-01,
       5.67690492e-01, 3.18215609e-01, 2.68611312e-02, 1.90313041e-01,
       1.18009746e-01, 3.33246291e-01, 5.38714945e-01, 7.59211779e-02,
       9.17032659e-01, 2.57328391e-01, 7.45061278e-01, 1.96683824e-01,
       2.07586229e-01, 7.18716383e-02, 3.18173170e-02, 8.40539217e-01,
       4.31627154e-01, 9.69988108e-02, 3.04359794e-02, 2.76549280e-01,
       2.97652543e-01, 9.99652743e-02, 6.43659174e-01, 2.97176778e-01,
       5.92178583e-01, 3.32788646e-01, 9.76564169e-01, 5.38676262e-01,
       8.16901386e-01, 1.34350538e-01, 1.91011310e-01, 1.48648024e-02,
       4.11586046e-01, 3.82653475e-01, 7.91540921e-01, 3.71671319e-02,
       6.66031003e-01, 2.66306400e-02, 7.54275322e-02, 8.06919932e-02,
       8.30547214e-02, 3.42482388e-01, 3.13050270e-01, 6.57553911e-01,
       2.11692393e-01, 5.95357418e-01, 3.81305814e-02, 1.94545865e-01,
       2.17068195e-02, 5.52969694e-01, 2.17236280e-02, 6.01660609e-02,
       4.34950173e-01, 5.11163533e-01, 1.10106707e-01, 6.15978837e-02,
       7.46262550e-01, 7.57325292e-02, 7.80862331e-01, 1.19389296e-01,
       9.07783508e-02, 9.61220264e-03, 2.94429898e-01, 3.49180460e-01,
       2.48019993e-01, 4.87697124e-03, 1.32755458e-01, 4.47140872e-01,
       5.28355181e-01, 7.83141255e-02, 3.45571041e-01, 4.67929900e-01,
       2.78728068e-01, 3.41981649e-03, 1.22354627e-01, 2.56370902e-02,
       2.71404982e-01, 2.14960158e-01, 4.85986292e-01, 1.59106612e-01,
       1.16984785e-01, 2.19153166e-02, 9.80026722e-02, 1.18314683e-01,
       2.91737080e-01, 7.38392949e-01, 1.21758699e-01, 2.76071429e-01,
       2.00586438e-01, 2.99319506e-01, 3.73648286e-01, 3.45361292e-01,
       7.39942789e-02, 2.80703306e-02, 2.76818514e-01, 2.37712860e-02,
       9.65909421e-01, 3.27037215e-01, 1.60051584e-02, 3.03239346e-01,
       4.27655280e-01, 8.46387327e-01, 5.82470894e-02, 7.68481493e-02,
       4.92456317e-01, 7.75352120e-02, 7.43094683e-02, 1.00456774e-01,
       8.42089415e-01, 3.04495454e-01, 2.06380844e-01, 1.81689382e-01,
       2.11482644e-02, 9.84551430e-01, 1.17933214e-01, 9.55976784e-01,
       3.23850989e-01, 1.01445317e-02, 8.12910199e-02, 7.30184913e-02,
       6.84743226e-01, 2.01350451e-01, 1.80177391e-01, 2.72841454e-01,
       2.01776743e-01, 7.14290142e-03, 7.29917288e-02, 3.22209477e-01,
       1.21977329e-02, 3.18226576e-01, 7.24093914e-02, 2.23963261e-02,
       7.05709457e-02, 8.55286717e-02, 2.78303564e-01, 9.13442552e-01,
       1.21366858e-01, 3.45485270e-01, 7.34769106e-02, 4.41897511e-02,
       7.92859793e-02, 3.87878418e-02, 1.42685771e-01, 3.52997899e-01,
       7.40594864e-02, 1.14634871e-01, 2.65707433e-01, 8.86160135e-01,
       4.79430735e-01, 7.96264648e-01, 5.31968117e-01, 1.12416267e-01,
       2.75421977e-01, 5.71388841e-01, 2.71451473e-02, 7.21479714e-01,
       7.64325261e-02, 2.73807228e-01, 2.34086573e-01, 7.14971423e-02,
       4.88296747e-02, 2.58206129e-02, 4.81342673e-02, 8.37628245e-02,
       9.92923379e-02, 7.56683350e-02, 4.09260631e-01, 3.44492435e-01,
       5.29805422e-02, 5.59499264e-02, 1.08626187e-01, 1.36322379e-02,
       4.74954426e-01, 1.38889611e-01, 1.21314108e-01, 5.38440943e-01,
       1.94435716e-02, 3.57758403e-02, 6.90191984e-03, 7.48628378e-02,
       7.68868923e-02, 3.62589836e-01, 8.23395848e-02, 2.70504951e-01,
       8.50817740e-01, 9.44007695e-01, 6.36070967e-02, 2.73464501e-01,
       8.28287005e-02, 7.56291747e-02, 7.62251616e-02, 8.49662364e-01,
       2.26657271e-01, 2.41519809e-02, 1.35746300e-01, 1.16817236e-01,
       8.40870023e-01, 3.40727568e-02, 7.45701194e-02, 7.71977901e-02,
       7.05448985e-02, 1.99838459e-01, 9.85240936e-02, 4.46765125e-01,
       8.56948256e-01, 1.39304817e-01, 5.41779995e-02, 1.36226952e-01,
       2.45562553e-01, 7.21552968e-01, 7.36066103e-02, 8.18928003e-01,
       3.77634764e-02, 1.88544393e-02, 2.45414317e-01, 3.66049409e-02,
       4.33453679e-01, 2.77645588e-02, 9.57614183e-02, 8.41775537e-02,
       1.46752596e-03, 1.77598000e-03, 3.58844936e-01, 7.77906179e-03,
       2.18895674e-01, 5.84685683e-01, 8.32410932e-01, 9.29060876e-01,
       3.61198187e-03, 8.75985503e-01, 7.87907839e-02, 6.56669497e-01,
       1.74642682e-01, 1.41378164e-01, 8.17596436e-01, 7.36174583e-02,
       6.54616356e-02, 4.80288267e-03, 7.80790865e-01, 3.89199853e-02,
       8.61450613e-01, 2.31072903e-02, 2.81322002e-03, 6.32055759e-01,
       1.00850463e-02, 2.23965704e-01, 5.81751108e-01, 1.11226439e-01,
       2.02445924e-01, 4.94601250e-01, 2.00682878e-03, 2.99788475e-01,
       1.03672206e-01, 3.35976481e-02, 3.43974233e-02, 2.25800872e-02,
       4.02169228e-02, 7.26744115e-01, 7.00284004e-01, 1.83476985e-01,
       5.53173423e-02, 3.96772504e-01, 3.30400109e-01, 7.22396374e-02,
       1.83567166e-01, 7.34453797e-02, 4.49116826e-02, 8.40321481e-01,
       5.17571449e-01, 6.41120553e-01, 8.08719397e-02, 3.66270542e-03,
       7.49320626e-01, 3.00007403e-01, 9.88627672e-01, 8.30161452e-01,
       1.90018296e-01, 3.76378894e-02, 3.92591357e-02, 8.13659430e-02,
       4.30179834e-02, 6.58023715e-01, 2.98702717e-03, 2.91805863e-02,
       2.91262031e-01, 2.78654099e-02, 1.11960113e-01, 5.52763343e-02,
       2.02624202e-02, 9.94300961e-01, 9.91734803e-01, 9.28206742e-01,
       9.49729025e-01, 4.49240088e-01, 4.22611654e-01, 6.42736554e-01,
       7.45348334e-02, 1.53545141e-02, 9.35352206e-01, 9.24548626e-01,
       2.27553427e-01, 2.53533959e-01, 3.03773880e-02, 9.67526436e-03,
       6.62066638e-01, 8.76794994e-01, 7.25036263e-02, 8.33667636e-01,
       3.21020484e-02, 5.92322350e-01, 1.37008011e-01, 6.58096671e-01,
       7.32969046e-02, 2.22892523e-01, 3.99278104e-01, 2.18923151e-01,
       2.60518491e-01, 8.87644291e-02, 5.93510866e-01, 7.31070638e-02,
       7.25361645e-01, 1.68046415e-01, 3.56008172e-01, 3.96980643e-02,
       7.98505545e-03, 6.87011123e-01, 1.57289743e-01, 2.34662175e-01,
       7.90798485e-01, 1.04982257e-02, 3.23050380e-01, 1.84250951e-01,
       7.30014443e-02, 9.80588675e-01, 1.41520321e-01, 3.48420322e-01,
       8.19414258e-02, 8.44500065e-02, 6.54957175e-01, 7.26554990e-02,
       7.08760619e-02, 8.40457678e-02, 7.39223599e-01, 3.68967056e-02,
       3.82151186e-01, 6.15385771e-02, 1.25381410e-01, 4.85122621e-01,
       2.20350087e-01, 7.74825335e-01, 7.25296736e-02, 1.27168417e-01,
       6.09356761e-02, 7.34324455e-02, 2.58154750e-01, 3.04088175e-01,
       7.29753971e-02, 2.43010044e-01, 7.16350675e-02, 2.65595198e-01,
       2.51342654e-02, 9.21941280e-01, 3.00366998e-01, 8.71148705e-02,
       2.34222531e-01, 8.48609924e-01, 9.60395336e-02, 2.17147470e-02,
       4.17438149e-02, 8.87052178e-01, 8.46701026e-01, 8.55739951e-01,
       1.17923021e-02, 5.18972278e-02, 3.40705812e-01, 3.35147440e-01,
       7.24768639e-02, 1.86657071e-01, 2.34130144e-01, 1.57754600e-01,
       3.55870485e-01, 1.92191482e-01, 6.51306629e-01, 4.00130033e-01,
       5.97188890e-01, 6.29841685e-01, 1.61570311e-03, 5.10001838e-01,
       2.59327888e-03, 2.01522112e-02, 4.63521242e-01, 7.84347653e-02,
       8.80602658e-01, 1.81099772e-02, 8.00765753e-01, 5.20564318e-02,
       9.90813255e-01, 1.79007649e-02, 9.81600821e-01, 4.05362248e-01,
       1.04390085e-01, 4.01831806e-01, 5.91386557e-02, 7.72060752e-02,
       7.73072243e-04, 5.19734025e-02, 1.15401983e-01, 3.92058492e-02,
       1.09988093e-01, 3.07213068e-02, 2.84661353e-01, 6.37609482e-01,
       2.39107907e-01, 2.62944043e-01, 2.62332559e-01, 5.50826430e-01,
       1.45849586e-01, 8.26735795e-01, 3.26709032e-01, 6.58282042e-02,
       7.18216300e-02, 4.78684008e-01, 3.18528295e-01, 5.82625568e-01,
       1.45905614e-01, 6.11297727e-01, 1.08888566e-01, 9.80460644e-03,
       7.23346829e-01, 1.39560699e-02, 9.55829024e-02, 2.41961181e-01,
       2.93614268e-01, 1.63172305e-01, 3.20041776e-02, 7.97787309e-02,
       7.66335309e-01, 7.24509597e-01, 4.85829711e-02, 3.45813334e-01,
       9.92902160e-01, 5.52470684e-01, 8.06453466e-01, 8.55754316e-01,
       7.46358633e-02, 7.30460882e-02, 9.97510970e-01, 1.65757537e-02,
       2.95215249e-02, 2.71694660e-02, 4.79956627e-01, 1.01028800e-01,
       8.40604305e-04, 9.98058736e-01, 8.39966536e-03, 6.86640143e-02,
       4.41053510e-02, 9.51468945e-03, 7.96165705e-01, 3.66886258e-02,
       1.73459470e-01, 2.82812119e-02, 5.45775890e-01, 6.45508587e-01,
       2.76347458e-01, 3.76747847e-02, 3.80495310e-01, 5.96114874e-01,
       1.53272629e-01, 2.12310493e-01, 7.27193952e-02, 1.12306356e-01,
       7.46285915e-03, 2.77400017e-02, 7.26745129e-02, 7.95308352e-02,
       8.49304259e-01, 2.63237774e-01, 3.96262407e-02, 5.12515903e-01,
       9.69351530e-02, 7.66542554e-02, 4.09018457e-01, 8.15015495e-01,
       6.45939112e-01, 1.64980710e-01, 5.56178689e-01, 4.16653037e-01,
       7.21203446e-01, 8.94374609e-01, 7.59984672e-01, 2.19715357e-01,
       1.76103175e-01, 5.16004622e-01, 5.32722592e-01, 1.54995978e-01,
       5.57866812e-01, 2.48772860e-01, 7.40729570e-02, 5.09268403e-01,
       3.70385051e-02, 9.48603153e-01, 2.72682548e-01, 4.34299707e-02,
       3.84621620e-02, 9.85504866e-01, 1.12743258e-01, 4.38834012e-01,
       2.05447674e-02, 5.27425647e-01, 7.51950741e-01, 1.73751831e-01,
       3.83408427e-01, 3.93769741e-02, 5.96148372e-02, 7.03900218e-01,
       1.28917038e-01, 4.49211001e-02, 6.25908315e-01, 2.55795002e-01,
       7.35210180e-02, 5.01587212e-01, 6.50774479e-01, 8.55933428e-01,
       3.53103876e-02, 8.41929317e-02, 1.02068841e-01, 1.38120115e-01,
       2.73369670e-01, 1.49786234e-01, 3.23570371e-01, 7.41534233e-02,
       8.87408972e-01, 8.52468014e-02, 8.23339045e-01, 2.83860683e-01,
       9.52463150e-02, 7.67214298e-02, 4.48670268e-01, 6.66022301e-03,
       2.48871088e-01, 4.30763364e-01, 1.72826648e-01, 3.58332992e-02,
       3.65472436e-02, 3.62135291e-01, 2.65438557e-02, 3.79775524e-01,
       8.55997741e-01, 4.54835892e-01, 9.99819279e-01, 7.79896498e-01,
       1.38051271e-01, 3.12645257e-01, 4.05034423e-02, 5.00106812e-02,
       1.04152501e-01, 8.44231844e-02, 4.14619684e-01, 7.53617883e-02,
       7.49919534e-01, 1.38085783e-01, 3.86130512e-01, 2.24514663e-01,
       6.63611889e-01, 7.94756413e-03, 4.26914096e-02, 2.15638280e-02,
       3.60714018e-01, 1.24937296e-03, 5.65639317e-01, 3.49276066e-02,
       3.18213701e-02, 4.62987423e-02, 1.92426562e-01, 5.50536335e-01,
       7.45326877e-02, 8.55688572e-01, 1.82104111e-01, 1.11275256e-01,
       8.52390110e-01, 5.10162711e-02, 2.97610760e-02, 9.66839790e-02,
       4.96022701e-01, 2.85663605e-01, 1.05978966e-01, 3.58005583e-01,
       7.07210898e-02, 2.60519981e-03, 1.86521471e-01, 3.47523093e-02,
       2.46352077e-01, 1.18136108e-01, 1.90917194e-01, 8.12498331e-02,
       8.38025570e-01, 2.08359063e-01, 1.97419107e-01, 2.57967114e-02,
       7.84887075e-02, 7.07113147e-02, 1.36036813e-01, 4.87959981e-02,
       9.60773349e-01, 6.91428959e-01, 9.83124137e-01, 4.31334555e-01,
       1.66880965e-01, 3.30543101e-01, 7.24697709e-02, 3.33594084e-02,
       1.09098673e-01, 4.34159577e-01, 7.56042004e-02, 7.31886029e-02,
       3.55049014e-01, 2.71476030e-01, 9.30047035e-03, 1.32780135e-01,
       2.20967770e-01, 8.48764181e-02, 6.75210714e-01, 9.60647464e-01,
       4.07025039e-01, 8.01545382e-03, 9.18323457e-01, 2.81987131e-01,
       4.73526955e-01, 2.46513188e-01, 2.64307261e-01, 5.92252851e-01,
       7.36116171e-02, 1.94527507e-02])

confidence_level = 0.8
threshold = np.quantile(calibration_nonconformity_scores, 1 - confidence_level)
print(f"Threshold for {confidence_level*100}% confidence level: {threshold}")


@app.route('/scoring', methods=['POST'])
def scoring():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400
    
    try:
        image = tf.io.decode_image(file.read(), channels=3)
        image = tf.image.resize(image, [224, 224])
        image = image / 255.0  # Normalize image
        image = tf.expand_dims(image, axis=0)  # Add batch dimension

        predictions = model.predict(image)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = predictions[0][predicted_class]
        reliability = get_conformal_prediction(predictions[0])

        response = {
            'predicted_class': int(predicted_class),
            'predicted_class_name': class_names[predicted_class],
            'confidence': float(confidence),
            'reliability': str(f"{reliability[0]}, {reliability[1]}")
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_conformal_prediction(predictions) -> list:
    max_p = np.max(predictions)
    nonconformity_score = 1 - max_p
    print(f"Nonconformity score: {nonconformity_score}")
    reliability_percentile = 1 - np.searchsorted(np.sort(calibration_nonconformity_scores), nonconformity_score) / len(calibration_nonconformity_scores)

    isReliable = nonconformity_score <= threshold
    return [isReliable, np.round(reliability_percentile, 2)]


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)