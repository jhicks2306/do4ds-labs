from vetiver import VetiverModel
import vetiver
import pins


b = pins.board_folder('/models/do4ds', allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'penguin_model')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
