from dotenv import load_dotenv

load_dotenv()

from vetiver import VetiverModel
import vetiver
import pins


b = pins.board_s3('do4ds-lab-s3', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model', version = '20240110T123044Z-73a81')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
