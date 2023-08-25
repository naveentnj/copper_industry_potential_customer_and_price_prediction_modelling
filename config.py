# Model Config
REGRESSION_MODEL_PATH = r"regression_models/regmodel2.pkl"
REGRESSION_SCALER = r"regression_models/scaler1.pkl"
REGRESSION_DATA_TRANSFORM = r"regression_models/transform.pkl"
REGRESSION_BINARY_ENC = r"regression_models/binary_enc.pkl"

CLASSIFICATION_MODEL_PATH = r"classification_models\classification_model1.pkl"
CLASSIFICATION_SCALER = r"classification_models\classification_scaler.pkl"
CLASSIFICATION_DATA_TRANSFORM = r"classification_models\classification_data_transform.pkl"

# APP Variables
status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
product=['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665', 
                '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407', 
                '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', 
                '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', 
                '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

title = """
<div style='text-align:center'>
    <h1 style='color:#009999;'>Industrial Copper Modeling Application</h1>
</div>
"""