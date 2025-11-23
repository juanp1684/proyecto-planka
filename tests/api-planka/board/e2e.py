
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.board_payloads import PAYLOAD_BOARD_CREATE 
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests





@pytest.mark.board
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_e2e_boards(setup_add_board,post_test_board):

   # =================================================
   #  Precondiciones: 
   # -  Usuario autenticado con credenciales validas
   # -  Token generado correctamente
   #=================================================

    # Creación de un nuevo tablero con los datos establecidos para el trabajo del equipo

    get_token,created_boards = setup_add_board
    url = EndpointPlanka.BASE_BOARDS.value
    TOKEN_PLANKA = get_token
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.post(url,headers,PAYLOAD_BOARD_CREATE)
    log_request_response(url, response, headers, PAYLOAD_BOARD_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    created_boards.append(response.json())



    # Obtener tablero creado recientemente

    url = EndpointPlanka.BASE_BOARDS_WITH_ID_BOARD.value
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)


    # Eliminar tablero no utilizado

    ID_BOARD =  post_test_board
    url = f"{EndpointPlanka.BASE_BOARD_MAJOR.value}/{ID_BOARD}"
    headers = {'Authorization': f'Bearer {TOKEN_PLANKA} '}
    response = PlankaRequests.delete(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)

