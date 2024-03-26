from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import io
import os;


#You can change these variables
font_size = 10;
font_file = "font.ttf";
colors = [[1,8,133], [0,0,255], [255,0,255], [0,255,255]];

document_data = {
        1:{
                "checkbox": [
                        {"coordinates": [36,716], "value": "X", "color": 0},
                ],
                "buyer_checkbox": [
                        {"coordinates": [36,172], "value": "X", "color": 0},
                        {"coordinates": [36,155], "value": "X", "color": 0},
                ],
                "seller_checkbox": [
                        {"coordinates": [75,172], "value": "X", "color": 0},
                        {"coordinates": [75,155], "value": "X", "color": 0},
                ],
                "landlord_checkbox": [
                        {"coordinates": [110,172], "value": "X", "color": 0},
                        {"coordinates": [110,155], "value": "X", "color": 0},
                ],
                "tenant_checkbox": [
                        {"coordinates": [157,172], "value": "X", "color": 0},
                        {"coordinates": [157,155], "value": "X", "color": 0},
                ],
                "buyer_1_name": [
                        {"coordinates": [200,172], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [200,155], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [505,172], "value": "X", "color": 0},
                        {"coordinates": [505,155], "value": "X", "color": 0},
                        {"coordinates": [505,116], "value": "X", "color": 0},
                ],
                "buyer_brokerage_name": [
                        {"coordinates": [63,137], "value": "X", "color": 0},
                ],
                "buyer_broker_name": [
                        {"coordinates": [53,116], "value": "X", "color": 0},
                ],
                "buyer_brokerage_number": [
                        {"coordinates": [485,137], "value": "X", "color": 0},
                ],
                "buyer_broker_number": [
                        {"coordinates": [404,116], "value": "X", "color": 0},
                ],
        },
        2:{

        },
        3:{

        },
        4:{
                "buyer_1_name": [
                        {"coordinates": [95,195], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [95,180], "value": "X", "color": 0},
                ],
                "seller_1_name": [
                        {"coordinates": [135,165], "value": "X", "color": 0},
                ],
                "seller_2_name": [
                        {"coordinates": [135,150], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [498,195], "value": "X", "color": 0},
                        {"coordinates": [498,180], "value": "X", "color": 0},
                        {"coordinates": [498,165], "value": "X", "color": 0},
                        {"coordinates": [498,150], "value": "X", "color": 0},
                ],
        },
        5:{
                "seller_1_name": [
                        {"coordinates": [75,320], "value": "X", "color": 0},
                        {"coordinates": [52,207], "value": "X", "color": 0},
                ],
                "seller_2_name": [
                        {"coordinates": [75,305], "value": "X", "color": 0},
                ],
                "buyer_1_name": [
                        {"coordinates": [75,290], "value": "X", "color": 0},
                        {"coordinates": [52,245], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [75,275], "value": "X", "color": 0},
                ],
                "buyer_brokerage_name": [
                        {"coordinates": [145,258], "value": "X", "color": 0},
                ],
                "seller_brokerage_name": [
                        {"coordinates": [145,221], "value": "X", "color": 0},
                ],
                "buyer_brokerage_number": [
                        {"coordinates": [437,258], "value": "X", "color": 0},
                ],
                "buyer_broker_number": [
                        {"coordinates": [437,245], "value": "X", "color": 0},
                ],
                "seller_brokerage_number": [
                        {"coordinates": [437,221], "value": "X", "color": 0},
                ],
                "seller_broker_number": [
                        {"coordinates": [437,207], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [516,320], "value": "X", "color": 0},
                        {"coordinates": [516,305], "value": "X", "color": 0},
                        {"coordinates": [516,290], "value": "X", "color": 0},
                        {"coordinates": [516,275], "value": "X", "color": 0},
                        {"coordinates": [516,245], "value": "X", "color": 0},
                        {"coordinates": [516,207], "value": "X", "color": 0},
                ],
        },
        6:{
                "buyer_1_name": [
                        {"coordinates": [105,245], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [105,227], "value": "X", "color": 0},
                ],
                "seller_1_name": [
                        {"coordinates": [111,210], "value": "X", "color": 0},
                ],
                "seller_2_name": [
                        {"coordinates": [111,190], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [509,245], "value": "X", "color": 0},
                        {"coordinates": [509,227], "value": "X", "color": 0},
                        {"coordinates": [509,210], "value": "X", "color": 0},
                        {"coordinates": [509,190], "value": "X", "color": 0},
                ],
        },
        7:{
                "buyer_1_name": [
                        {"coordinates": [70,200], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [70,180], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [492,200], "value": "X", "color": 0},
                        {"coordinates": [492,180], "value": "X", "color": 0},
                ],
        },
        8:{
                "date_prepared": [
                        {"coordinates": [100,710], "value": "X", "color": 0},
                ],
                "buyer_1_name": [
                        {"coordinates": [185,689], "value": "X", "color": 0},
                ],
                "property_address": [
                        {"coordinates": [215,677], "value": "X", "color": 0},
                ],
                "property_city": [
                        {"coordinates": [83,666], "value": "X", "color": 0},
                ],
                "property_county": [
                        {"coordinates": [250,666], "value": "X", "color": 0},
                ],
                "property_zip": [
                        {"coordinates": [467,666], "value": "X", "color": 0},
                ],
                "property_apn": [
                        {"coordinates": [175,655], "value": "X", "color": 0},
                ],
                "seller_brokerage_name": [
                        {"coordinates": [180,568], "value": "X", "color": 0},
                ],
                "seller_brokerage_number": [
                        {"coordinates": [500,568], "value": "X", "color": 0},
                ],
                "seller_broker_name": [
                        {"coordinates": [132,545], "value": "X", "color": 0},
                ],
                "seller_broker_number": [
                        {"coordinates": [500,545], "value": "X", "color": 0},
                ],
                "buyer_brokerage_name": [
                        {"coordinates": [180,522], "value": "X", "color": 0},
                ],
                "buyer_brokerage_number": [
                        {"coordinates": [500,522], "value": "X", "color": 0},
                ],
                "buyer_broker_name": [
                        {"coordinates": [136,501], "value": "X", "color": 0},
                ],
                "buyer_broker_number": [
                        {"coordinates": [500,500], "value": "X", "color": 0},
                ],
                "brokerage_seller_checkbox": [
                        {"coordinates": [190,558], "value": "X", "color": 0},
                ],
                "brokerage_seller_dual_checkbox": [
                        {"coordinates": [258,558], "value": "X", "color": 0},
                ],
                "broker_seller_checkbox": [
                        {"coordinates": [133,534], "value": "X", "color": 0},
                ],
                "broker_seller_dual_checkbox": [
                        {"coordinates": [370,534], "value": "X", "color": 0},
                ],
                "brokerage_buyer_checkbox": [
                        {"coordinates": [189,512], "value": "X", "color": 0},
                ],
                "brokerage_buyer_dual_checkbox": [
                        {"coordinates": [259,512], "value": "X", "color": 0},
                ],
                "broker_buyer_checkbox": [
                        {"coordinates": [134,488], "value": "X", "color": 0},
                ],
                "broker_buyer_dual_checkbox": [
                        {"coordinates": [371,488], "value": "X", "color": 0},
                ],
                "more_brokerage_checkbox": [
                        {"coordinates": [72,478], "value": "X", "color": 0},
                ],
                "more_brokerage_seller_checkbox": [
                        {"coordinates": [232,478], "value": "X", "color": 0},
                ],
                "more_brokerage_buyer_checkbox": [
                        {"coordinates": [270,478], "value": "X", "color": 0},
                ],
                "competing_checkbox": [
                        {"coordinates": [525,466], "value": "X", "color": 0},
                ],
                "purchase_price": [
                        {"coordinates": [279,402], "value": "X", "color": 0},
                ],
                "all_cash_checkbox": [
                        {"coordinates": [455,402], "value": "X", "color": 0},
                ],
                "escrow_days": [
                        {"coordinates": [287,387], "value": "X", "color": 0},
                ],
                "escrow_days_checkbox": [
                        {"coordinates": [272,387], "value": "X", "color": 0},
                ],
                "escrow_date_checkbox": [
                        {"coordinates": [298,378], "value": "X", "color": 0},
                ],
                "escrow_date_line": [
                        {"coordinates": [311,377], "value": "X", "color": 0},
                ],
                "expiration_date": [
                        {"coordinates": [281,355], "value": "X", "color": 0},
                ],
                "expiration_time": [
                        {"coordinates": [308,346], "value": "X", "color": 0},
                ],
                "expiration_am_checkbox": [
                        {"coordinates": [335,345], "value": "X", "color": 0},
                ],
                "expiration_pm_checkbox": [
                        {"coordinates": [361,345], "value": "X", "color": 0},
                ],
                "initial_deposit": [
                        {"coordinates": [277,330], "value": "X", "color": 0},
                ],
                "initial_deposit_percentage": [
                        {"coordinates": [338,330], "value": "X", "color": 0},
                ],
                "initial_deposit_days": [
                        {"coordinates": [499,332], "value": "X", "color": 0},
                ],
                "initial_deposit_or_checkbox": [
                        {"coordinates": [470,313], "value": "X", "color": 0},
                ],
                "intial_deposit_or_line": [
                        {"coordinates": [496,313], "value": "X", "color": 0},
                ],
                "increased_deposit_checkbox": [
                        {"coordinates": [128,300], "value": "X", "color": 0},
                ],
                "increased_deposit": [
                        {"coordinates": [279,300], "value": "X", "color": 0},
                ],
                "increased_deposit_percent": [
                        {"coordinates": [338,300], "value": "X", "color": 0},
                ],
                "increased_deposit_or_checkbox": [
                        {"coordinates": [470,291], "value": "X", "color": 0},
                        {"coordinates": [470,276], "value": "X", "color": 0},
                ],
                "increased_deposit_or_date": [
                        {"coordinates": [487,290], "value": "X", "color": 0},
                ],
                "increased_deposit_or_line": [
                        {"coordinates": [486,276], "value": "X", "color": 0},
                ],
                "loan_amount": [
                        {"coordinates": [279,260], "value": "X", "color": 0},
                ],
                "loan_percent": [
                        {"coordinates": [339,260], "value": "X", "color": 0},
                ],
                "laon_initial_adjustable_rate_checkbox": [
                        {"coordinates": [319,251], "value": "X", "color": 0},
                ],
                "loan_exceed_percent": [
                        {"coordinates": [338,243], "value": "X", "color": 0},
                ],
                "loan_buyer_points": [
                        {"coordinates": [355,232], "value": "X", "color": 0},
                ],
                "loan_days_acceptance": [
                        {"coordinates": [298,207], "value": "X", "color": 0},
                ],
                "loan_fha_checkbox": [
                        {"coordinates": [455,246], "value": "X", "color": 0},
                ],
                "loan_va_checkbox": [
                        {"coordinates": [455,237], "value": "X", "color": 0},
                ],
                "loan_seller_financing_checkbox": [
                        {"coordinates": [455,228], "value": "X", "color": 0},
                ],
                "other_checkbox": [
                        {"coordinates": [455,218], "value": "X", "color": 0},
                ],
                "other_line": [
                        {"coordinates": [464,206], "value": "X", "color": 0},
                ],
                "additional_financed_amount": [
                        {"coordinates": [278,180], "value": "X", "color": 0},
                ],
                "additional_financed_percent": [
                        {"coordinates": [338,180], "value": "X", "color": 0},
                ],
                "additional_adjustable_rate_checkbox": [
                        {"coordinates": [319,169], "value": "X", "color": 0},
                ],
                "additional_exceed_percent": [
                        {"coordinates": [332,160], "value": "X", "color": 0},
                ],
                "additional_points": [
                        {"coordinates": [352,151], "value": "X", "color": 0},
                ],
                "additional_seller_financing_checkbox": [
                        {"coordinates": [455,174], "value": "X", "color": 0},
                ],
                "additional_other_checkbox": [
                        {"coordinates": [455,164], "value": "X", "color": 0},
                ],
                "additional_other_line": [
                        {"coordinates": [464,154], "value": "X", "color": 0},
                ],
                "occupancy_secondary_checkbox": [
                        {"coordinates": [353,129], "value": "X", "color": 0},
                ],
                "occupancy_investment_checkbox": [
                        {"coordinates": [405,129], "value": "X", "color": 0},
                ],
                "balance_down_payment": [
                        {"coordinates": [280,117], "value": "X", "color": 0},
                ],
                "purchase_price_total": [
                        {"coordinates": [280,103], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,67], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [345,67], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [462,67], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [508,67], "value": "X", "color": 0},
                ],
        },
        9:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [464,768], "value": "X", "color": 0},
                ],
                "seller_credit_checkbox": [
                        {"coordinates": [272,733], "value": "X", "color": 0},
                ],
                "seller_credit_amount": [
                        {"coordinates": [290,733], "value": "X", "color": 0},
                ],
                "seller_credit_percent": [
                        {"coordinates": [340,733], "value": "X", "color": 0},
                ],
                "seller_credit_other_checkbox": [
                        {"coordinates": [491,724], "value": "X", "color": 0},
                ],
                "seller_credit_other_line": [
                        {"coordinates": [459,714], "value": "X", "color": 0},
                ],
                "additional_finance_terms_line1": [
                        {"coordinates": [199,703], "value": "X", "color": 0},
                ],
                "additional_finance_terms_line2": [
                        {"coordinates": [74,694], "value": "X", "color": 0},
                ],
                "seller_agree_checkbox": [
                        {"coordinates": [131,680], "value": "X", "color": 0},
                ],
                "verification_cash_or_checkbox": [
                        {"coordinates": [355,654], "value": "X", "color": 0},
                ],
                "verification_cash_or_days": [
                        {"coordinates": [384,654], "value": "X", "color": 0},
                ],
                "verification_down_or_checkbox": [
                        {"coordinates": [355,630], "value": "X", "color": 0},
                ],
                "verification_down_or_days": [
                        {"coordinates": [385,630], "value": "X", "color": 0},
                ],
                "verification_loan_checkbox": [
                        {"coordinates": [355,603], "value": "X", "color": 0},
                ],
                "verification_loan_days": [
                        {"coordinates": [384,602], "value": "X", "color": 0},
                ],
                "prequalifcation_checkbox": [
                        {"coordinates": [455,604], "value": "X", "color": 0},
                ],
                "preapproval_checkbox": [
                        {"coordinates": [522,603], "value": "X", "color": 0},
                ],
                "underwritten_preapproval_checkbox": [
                        {"coordinates": [455,594], "value": "X", "color": 0},
                ],
                "final_verification_days": [
                        {"coordinates": [290,570], "value": "X", "color": 0},
                ],
                "assignment_request_days": [
                        {"coordinates": [295,556], "value": "X", "color": 0},
                ],
                "loans_days": [
                        {"coordinates": [296,528], "value": "X", "color": 0},
                ],
                "no_loan_contingency_checkbox": [
                        {"coordinates": [455,529], "value": "X", "color": 0},
                ],
                "appraisal_checkbox": [
                        {"coordinates": [131,487], "value": "X", "color": 0},
                ],
                "appraisal_amount": [
                        {"coordinates": [150,486], "value": "X", "color": 0},
                ],
                "appraisal_days": [
                        {"coordinates": [295,514], "value": "X", "color": 0},
                ],
                "no_appraisal_contingency_checkbox": [
                        {"coordinates": [455,513], "value": "X", "color": 0},
                ],
                "investigation_of_property_days": [
                        {"coordinates": [295,469], "value": "X", "color": 0},
                ],
                "informal_access_to_property_days": [
                        {"coordinates": [295,455], "value": "X", "color": 0},
                ],
                "review_of_seller_documents_days": [
                        {"coordinates": [294,421], "value": "X", "color": 0},
                ],
                "preliminary_report_days": [
                        {"coordinates": [295,398], "value": "X", "color": 0},
                ],
                "common_interest_disclosures_days": [
                        {"coordinates": [295,376], "value": "X", "color": 0},
                ],
                "review_of_leased_or_liened_items_days": [
                        {"coordinates": [295,345], "value": "X", "color": 0},
                ],
                "crb_attached_checkbox": [
                        {"coordinates": [489,346], "value": "X", "color": 0},
                ],
                "car_form_cop_attached_checkbox": [
                        {"coordinates": [468,313], "value": "X", "color": 0},
                ],
                "time_possesion_checkbox": [
                        {"coordinates": [384,285], "value": "X", "color": 0},
                ],
                "time_possession_time": [
                        {"coordinates": [272,276], "value": "X", "color": 0},
                ],
                "time_position_am_checkbox": [
                        {"coordinates": [296,276], "value": "X", "color": 0},
                ],
                "time_position_pm_checkbox": [
                        {"coordinates": [322,276], "value": "X", "color": 0},
                ],
                "seller_occupied_coe_29_checkbox": [
                        {"coordinates": [272,246], "value": "X", "color": 0},
                ],
                "seller_occupied_coe_29_days": [
                        {"coordinates": [281,247], "value": "X", "color": 0},
                ],
                "seller_occupied_coe_30_checkbox": [
                        {"coordinates": [272,236], "value": "X", "color": 0},
                ],
                "seller_occupied_coe_30_days": [
                        {"coordinates": [281,236], "value": "X", "color": 0},
                ],
                "tenant_occupied_checkbox": [
                        {"coordinates": [272,222], "value": "X", "color": 0},
                ],
                "seller_delivery_documents_days": [
                        {"coordinates": [292,159], "value": "X", "color": 0},
                ],
                "escrow_holder_sign_days": [
                        {"coordinates": [292,145], "value": "X", "color": 0},
                ],
                "time_to_pay_fees_hoa_days": [
                        {"coordinates": [292,124], "value": "X", "color": 0},
                ],
                "install_smoke_alarms_days": [
                        {"coordinates": [292,101], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [295,50], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [340,51], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [464,50], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [507,50], "value": "X", "color": 0},
                ],
        },
        10:{
                "property_address": [
                        {"coordinates": [110,768], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [466,768], "value": "X", "color": 0},
                ],
                "stove_checkbox": [
                        {"coordinates": [128,716], "value": "X", "color": 0},
                ],
                "refridgerators_checkbox": [
                        {"coordinates": [128,700], "value": "X", "color": 0},
                ],
                "wine_refridgerators_checkbox": [
                        {"coordinates": [128,690], "value": "X", "color": 0},
                ],
                "washers_checkbox": [
                        {"coordinates": [128,681], "value": "X", "color": 0},
                ],
                "dryers_checkbox": [
                        {"coordinates": [128,673], "value": "X", "color": 0},
                ],
                "dishwashers_checkbox": [
                        {"coordinates": [128,663], "value": "X", "color": 0},
                ],
                "microwaves_checkbox": [
                        {"coordinates": [128,653], "value": "X", "color": 0},
                ],
                "additional_checkbox": [
                        {"coordinates": [128,632], "value": "X", "color": 0},
                        {"coordinates": [270,643], "value": "X", "color": 0},
                        {"coordinates": [270,632], "value": "X", "color": 0},
                        {"coordinates": [443,643], "value": "X", "color": 0},
                        {"coordinates": [443,632], "value": "X", "color": 0},
                ],
                "additional_item": [
                        {"coordinates": [140,632], "value": "X", "color": 0},
                        {"coordinates": [281,642], "value": "X", "color": 0},
                        {"coordinates": [283,632], "value": "X", "color": 0},
                        {"coordinates": [458,642], "value": "X", "color": 0},
                        {"coordinates": [457,632], "value": "X", "color": 0},
                ],
                "video_doorbell_checkbox": [
                        {"coordinates": [270,717], "value": "X", "color": 0},
                ],
                "security_camera_checkbox": [
                        {"coordinates": [270,708], "value": "X", "color": 0},
                ],
                "security_systems_checkbox": [
                        {"coordinates": [270,698], "value": "X", "color": 0},
                ],
                "smart_home_checkbox": [
                        {"coordinates": [270,673], "value": "X", "color": 0},
                ],
                "wall_mounted_checkbox": [
                        {"coordinates": [270,663], "value": "X", "color": 0},
                ],
                "above_ground_pool_checkbox": [
                        {"coordinates": [443,716], "value": "X", "color": 0},
                ],
                "bathroom_mirrors_checkbox": [
                        {"coordinates": [443,707], "value": "X", "color": 0},
                ],
                "electric_car_charger_checkbox": [
                        {"coordinates": [443,690], "value": "X", "color": 0},
                ],
                "potted_trees_checkbox": [
                        {"coordinates": [443,672], "value": "X", "color": 0},
                ],
                "spas_checkbox": [
                        {"coordinates": [536,716], "value": "X", "color": 0},
                ],
                "excluded_checkbox": [
                        {"coordinates": [127,602], "value": "X", "color": 0},
                        {"coordinates": [270,602], "value": "X", "color": 0},
                        {"coordinates": [443,602], "value": "X", "color": 0},
                ],
                "excluded_item": [
                        {"coordinates": [138,602], "value": "X", "color": 0},
                        {"coordinates": [283,602], "value": "X", "color": 0},
                        {"coordinates": [456,602], "value": "X", "color": 0},
                ],
                "natural_hazard_buyer_checkbox": [
                        {"coordinates": [272,553], "value": "X", "color": 0},
                ],
                "natural_hazard_seller_checkbox": [
                        {"coordinates": [306,553], "value": "X", "color": 0},
                ],
                "natural_hazard_both_checkbox": [
                        {"coordinates": [341,553], "value": "X", "color": 0},
                ],
                "natural_hazard_both_line_1": [
                        {"coordinates": [370,553], "value": "X", "color": 0},
                ],
                "natural_hazard_both_line_2": [
                        {"coordinates": [274,545], "value": "X", "color": 0},
                ],
                "natural_hazard_both_line_3": [
                        {"coordinates": [274,534], "value": "X", "color": 0},
                ],
                "natural_hazard_environmental_checkbox": [
                        {"coordinates": [456,553], "value": "X", "color": 0},
                ],
                "natural_hazard_other_checkbox": [
                        {"coordinates": [456,544], "value": "X", "color": 0},
                ],
                "natural_hazard_other_line_1": [
                        {"coordinates": [494,544], "value": "X", "color": 0},
                ],
                "natural_hazard_provided_checkbox": [
                        {"coordinates": [272,520], "value": "X", "color": 0},
                ],
                "natural_hazard_provided_line": [
                        {"coordinates": [329,520], "value": "X", "color": 0},
                ],
                "item_description_line": [
                        {"coordinates": [130,506], "value": "X", "color": 0},
                ],
                "item_description_buyer_checkbox": [
                        {"coordinates": [272,506], "value": "X", "color": 0},
                ],
                "item_description_seller_checkbox": [
                        {"coordinates": [306,506], "value": "X", "color": 0},
                ],
                "item_description_both_checkbox": [
                        {"coordinates": [341,506], "value": "X", "color": 0},
                ],
                "item_description_both_line_1": [
                        {"coordinates": [370,506], "value": "X", "color": 0},
                ],
                "item_description_provided": [
                        {"coordinates": [325,493], "value": "X", "color": 0},
                ],
                "item_report_line": [
                        {"coordinates": [130,479], "value": "X", "color": 0},
                ],
                "item_report_buyer_checkbox": [
                        {"coordinates": [272,479], "value": "X", "color": 0},
                ],
                "item_report_seller_checkbox": [
                        {"coordinates": [306,478], "value": "X", "color": 0},
                ],
                "item_report_both_checkbox": [
                        {"coordinates": [340,478], "value": "X", "color": 0},
                ],
                "item_report_both_line": [
                        {"coordinates": [370,480], "value": "X", "color": 0},
                ],
                "detectors_buyer_checkbox": [
                        {"coordinates": [272,464], "value": "X", "color": 0},
                ],
                "detectors_seller_checkbox": [
                        {"coordinates": [306,464], "value": "X", "color": 0},
                ],
                "detectors_both_checkbox": [
                        {"coordinates": [341,464], "value": "X", "color": 0},
                ],
                "detectors_both_line": [
                        {"coordinates": [370,464], "value": "X", "color": 0},
                ],
                "inspections_buyer_checkbox": [
                        {"coordinates": [272,445], "value": "X", "color": 0},
                ],
                "inspections_seller_checkbox": [
                        {"coordinates": [306,445], "value": "X", "color": 0},
                ],
                "inspections_both_checkbox": [
                        {"coordinates": [341,445], "value": "X", "color": 0},
                ],
                "inspections_both_line": [
                        {"coordinates": [370,445], "value": "X", "color": 0},
                ],
                "corrective_buyer_checkbox": [
                        {"coordinates": [272,424], "value": "X", "color": 0},
                ],
                "corrective_seller_checkbox": [
                        {"coordinates": [306,424], "value": "X", "color": 0},
                ],
                "corrective_both_checkbox": [
                        {"coordinates": [340,424], "value": "X", "color": 0},
                ],
                "corrective_both_line": [
                        {"coordinates": [370,424], "value": "X", "color": 0},
                ],
                "escrow_fee_buyer_checkbox": [
                        {"coordinates": [271,403], "value": "X", "color": 0},
                ],
                "escrow_fee_seller_checkbox": [
                        {"coordinates": [306,402], "value": "X", "color": 0},
                ],
                "escrow_fee_both_checkbox": [
                        {"coordinates": [340,403], "value": "X", "color": 0},
                ],
                "escrow_fee_both_line": [
                        {"coordinates": [370,403], "value": "X", "color": 0},
                ],
                "escrow_fee_each_checkbox": [
                        {"coordinates": [450,403], "value": "X", "color": 0},
                ],
                "escrow_holder_line": [
                        {"coordinates": [332,391], "value": "X", "color": 0},
                ],
                "insurance_buyer_checkbox": [
                        {"coordinates": [271,375], "value": "X", "color": 0},
                ],
                "insurance_seller_checkbox": [
                        {"coordinates": [306,375], "value": "X", "color": 0},
                ],
                "insurance_both_checkbox": [
                        {"coordinates": [341,375], "value": "X", "color": 0},
                ],
                "insurance_both_line": [
                        {"coordinates": [370,376], "value": "X", "color": 0},
                ],
                "insurance_title_co": [
                        {"coordinates": [429,364], "value": "X", "color": 0},
                ],
                "county_transfer_buyer_checkbox": [
                        {"coordinates": [272,319], "value": "X", "color": 0},
                ],
                "county_transfer_seller_checkbox": [
                        {"coordinates": [306,319], "value": "X", "color": 0},
                ],
                "county_transfer_both_checkbox": [
                        {"coordinates": [341,319], "value": "X", "color": 0},
                ],
                "county_transfer_both_line": [
                        {"coordinates": [370,318], "value": "X", "color": 0},
                ],
                "city_transfer_buyer_checkbox": [
                        {"coordinates": [272,305], "value": "X", "color": 0},
                ],
                "city_transfer_seller_checkbox": [
                        {"coordinates": [306,304], "value": "X", "color": 0},
                ],
                "city_transfer_both_checkbox": [
                        {"coordinates": [341,305], "value": "X", "color": 0},
                ],
                "city_transfer__both_line": [
                        {"coordinates": [370,305], "value": "X", "color": 0},
                ],
                "hao_transfer_buyer_checkbox": [
                        {"coordinates": [272,265], "value": "X", "color": 0},
                ],
                "hoa_transfer_seller_checkbox": [
                        {"coordinates": [307,263], "value": "X", "color": 0},
                ],
                "hoa_transfer_both_checkbox": [
                        {"coordinates": [341,263], "value": "X", "color": 0},
                ],
                "hoa_transfer_both_line": [
                        {"coordinates": [370,264], "value": "X", "color": 0},
                ],
                "private_transfer_buyer_checkbox": [
                        {"coordinates": [346,209], "value": "X", "color": 0},
                ],
                "private_transfer_both_checkbox": [
                        {"coordinates": [379,209], "value": "X", "color": 0},
                ],
                "private_transfer_both_line": [
                        {"coordinates": [276,197], "value": "X", "color": 0},
                ],
                "item1_fees_line": [
                        {"coordinates": [131,183], "value": "X", "color": 0},
                ],
                "item1_fees_buyer_checkbox": [
                        {"coordinates": [272,182], "value": "X", "color": 0},
                ],
                "item1_fees_seller_checkbox": [
                        {"coordinates": [306,182], "value": "X", "color": 0},
                ],
                "item1_fees_both_checkbox": [
                        {"coordinates": [341,182], "value": "X", "color": 0},
                ],
                "item1_fees_both_line": [
                        {"coordinates": [370,182], "value": "X", "color": 0},
                ],
                "item2_fees_line": [
                        {"coordinates": [131,169], "value": "X", "color": 0},
                ],
                "item2_fees_buyer_checkbox": [
                        {"coordinates": [271,169], "value": "X", "color": 0},
                ],
                "item2_fees_seller_checkbox": [
                        {"coordinates": [306,168], "value": "X", "color": 0},
                ],
                "item2_fees_both_checkbox": [
                        {"coordinates": [340,168], "value": "X", "color": 0},
                ],
                "item2_fees_both_line": [
                        {"coordinates": [370,169], "value": "X", "color": 0},
                ],
                "warranty_plan_item1": [
                        {"coordinates": [132,138], "value": "X", "color": 0},
                ],
                "warranty_plan_item2": [
                        {"coordinates": [132,127], "value": "X", "color": 0},
                ],
                "warranty_plan_item3": [
                        {"coordinates": [132,115], "value": "X", "color": 0},
                ],
                "warranty_plan_buyer_checkbox": [
                        {"coordinates": [272,156], "value": "X", "color": 0},
                ],
                "warranty_plan_seller_checkbox": [
                        {"coordinates": [306,156], "value": "X", "color": 0},
                ],
                "warranty_plan_both_checkbox": [
                        {"coordinates": [341,156], "value": "X", "color": 0},
                ],
                "warranty_plan_both_line": [
                        {"coordinates": [370,156], "value": "X", "color": 0},
                ],
                "warranty_plan_exceed_price": [
                        {"coordinates": [526,146], "value": "X", "color": 0},
                ],
                "warranty_plan_issued_by": [
                        {"coordinates": [313,136], "value": "X", "color": 0},
                ],
                "warranty_plan_buyer_waives_checkbox": [
                        {"coordinates": [272,123], "value": "X", "color": 0},
                ],
                "other_terms_line_1": [
                        {"coordinates": [141,103], "value": "X", "color": 0},
                ],
                "other_terms_line_2": [
                        {"coordinates": [78,92], "value": "X", "color": 0},
                ],
                "other_terms_line_3": [
                        {"coordinates": [78,81], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [296,49], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [343,49], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [462,49], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [506,49], "value": "X", "color": 0},
                ],
        },
        11:{
                "property_address": [
                        {"coordinates": [113,768], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [468,768], "value": "X", "color": 0},
                ],
                "tenant_occupied_property_addendum_checkbox": [
                        {"coordinates": [72,737], "value": "X", "color": 0},
                ],
                "probate_agreement_purchase_addendum_checkbox": [
                        {"coordinates": [72,726], "value": "X", "color": 0},
                ],
                "manufactured_home_purchase_addendum_checkbox": [
                        {"coordinates": [72,715], "value": "X", "color": 0},
                ],
                "tenancy_in_common_purchase_addendum_checkbox": [
                        {"coordinates": [72,702], "value": "X", "color": 0},
                ],
                "stock_cooperative_purchase_addendum_checkbox": [
                        {"coordinates": [72,691], "value": "X", "color": 0},
                ],
                "mixed_use_purchase_addendum_checkbox": [
                        {"coordinates": [72,680], "value": "X", "color": 0},
                ],
                "other_a_checkbox": [
                        {"coordinates": [314,680], "value": "X", "color": 0},
                ],
                "other_a_line" :[
                        {"coordinates": [351,680], "value": "X", "color": 0},
                ],
                "addendum_checkbox": [
                        {"coordinates": [72,659], "value": "X", "color": 0},
                ],
                "addendum_number": [
                        {"coordinates": [140,660], "value": "X", "color": 0},
                ],
                "back_up_offer_addendum_checkbox": [
                        {"coordinates": [72,648], "value": "X", "color": 0},
                ],
                "septic_well_property_mountained_and_propane_addendum_checkbox": [
                        {"coordinates": [72,637], "value": "X", "color": 0},
                ],
                "buyer_intent_to_exchange_addendum_checkbox": [
                        {"coordinates": [72,625], "value": "X", "color": 0},
                ],
                "short_sale_addendum_checkbox": [
                        {"coordinates": [314,660], "value": "X", "color": 0},
                ],
                "court_confirmation_addendum_checkbox": [
                        {"coordinates": [314,648], "value": "X", "color": 0},
                ],
                "seller_intent_to_exchange_addendum_checkbox": [
                        {"coordinates": [314,626], "value": "X", "color": 0},
                ],
                "other_b_checkbox": [
                        {"coordinates": [72,614], "value": "X", "color": 0},
                        {"coordinates": [314,615], "value": "X", "color": 0},
                ],
                "other_b_line": [
                        {"coordinates": [110,615], "value": "X", "color": 0},
                        {"coordinates": [351,615], "value": "X", "color": 0},
                ],
                "buyer_investigation_advisory_checkbox": [
                        {"coordinates": [72,582], "value": "X", "color": 0},
                ],
                "wire_fraud_advisory_checkbox": [
                        {"coordinates": [72,571], "value": "X", "color": 0},
                ],
                "wildfire_disaster_advisory_checkbox": [
                        {"coordinates": [72,551], "value": "X", "color": 0},
                ],
                "trust_advisory_checkbox": [
                        {"coordinates": [72,540], "value": "X", "color": 0},
                ],
                "reo_advisory_checkbox": [
                        {"coordinates": [72,529], "value": "X", "color": 0},
                ],
                "fair_housing_and_discrimination_advisory_checkbox": [
                        {"coordinates": [314,582], "value": "X", "color": 0},
                ],
                "consumer_privacy_act_advisory_checkbox": [
                        {"coordinates": [314,570], "value": "X", "color": 0},
                ],
                "statewide_buyer_and_seller_advisory_checkbox": [
                        {"coordinates": [314,551], "value": "X", "color": 0},
                ],
                "short_sale_information_and_advisory_checkbox": [
                        {"coordinates": [314,540], "value": "X", "color": 0},
                ],
                "probate_advisory_checkbox": [
                        {"coordinates": [314,529], "value": "X", "color": 0},
                ],
                "other_c_checkbox": [
                        {"coordinates": [72,518], "value": "X", "color": 0},
                        {"coordinates": [314,518], "value": "X", "color": 0},
                ],
                "other_c_line": [
                        {"coordinates": [110,518], "value": "X", "color": 0},
                        {"coordinates": [351,518], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [298,47], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [345,47], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [462,47], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [505,47], "value": "X", "color": 0},
                ],
        },
        12:{
                "property_address": [
                        {"coordinates": [111,768], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [466,768], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,47], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,47], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,47], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,47], "value": "X", "color": 0},
                ],
        },
        13:{
                "property_address": [
                        {"coordinates": [112,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [467,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,46], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,46], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,46], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,46], "value": "X", "color": 0},
                ],
        },
        14:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,48], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,48], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,48], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,48], "value": "X", "color": 0},
                ],
        },
        15:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,54], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,54], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,54], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,54], "value": "X", "color": 0},
                ],
        },
        16:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,50], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,50], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,50], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,50], "value": "X", "color": 0},
                ],
        },
        17:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,45], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,45], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,45], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,45], "value": "X", "color": 0},
                ],
        },
        18:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,45], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,45], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,45], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,45], "value": "X", "color": 0},
                ],
        },
        19:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,46], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,46], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,46], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,46], "value": "X", "color": 0},
                ],
        },
        20:{
                "property_address": [
                        {"coordinates": [110,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [465,767], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [300,50], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [350,50], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [470,50], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [510,50], "value": "X", "color": 0},
                ],
        },
        21:{
                "property_address": [
                        {"coordinates": [111,768], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [468,768], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [200,598], "value": "X", "color": 0},
                        {"coordinates": [201,82], "value": "X", "color": 0},
                        {"coordinates": [297,46], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [245,598], "value": "X", "color": 0},
                        {"coordinates": [244,82], "value": "X", "color": 0},
                        {"coordinates": [344,46], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [437,598], "value": "X", "color": 0},
                        {"coordinates": [438,82], "value": "X", "color": 0},
                        {"coordinates": [461,46], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [479,598], "value": "X", "color": 0},
                        {"coordinates": [479,82], "value": "X", "color": 0},
                        {"coordinates": [508,46], "value": "X", "color": 0},
                ],
        },
        22:{
                "property_address": [
                        {"coordinates": [113,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [469,768], "value": "X", "color": 0},
                        {"coordinates": [503,542], "value": "X", "color": 0},
                        {"coordinates": [503,502], "value": "X", "color": 0},
                        {"coordinates": [503,193], "value": "X", "color": 0},
                        {"coordinates": [503,154], "value": "X", "color": 0},
                ],
                "entity_buyers_checkbox": [
                        {"coordinates": [72,713], "value": "X", "color": 0},
                ],
                "authorized_signer_names": [
                        {"coordinates": [325,658], "value": "X", "color": 0},
                        {"coordinates": [317,307], "value": "X", "color": 0},
                ],
                "fullname_line_1": [
                        {"coordinates": [95,612], "value": "X", "color": 0},
                ],
                "fullname_line_2": [
                        {"coordinates": [95,602], "value": "X", "color": 0},
                ],
                "fullname_line_3": [
                        {"coordinates": [95,591], "value": "X", "color": 0},
                ],
                "buyer1_name": [
                        {"coordinates": [119,543], "value": "X", "color": 0},
                        {"coordinates": [178,531], "value": "X", "color": 0},
                ],
                "buyer1_name_signer_checkbox": [
                        {"coordinates": [72,517], "value": "X", "color": 0},
                ],
                "buyer1_name_signer": [
                        {"coordinates": [263,517], "value": "X", "color": 0},
                ],
                "buyer1_name_signer_title": [
                        {"coordinates": [503,518], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [119,504], "value": "X", "color": 0},
                        {"coordinates": [178,490], "value": "X", "color": 0},
                ],
                "buyer_2_name_signer_checkbox": [
                        {"coordinates": [72,477], "value": "X", "color": 0},
                ],
                "buyer_2_name_signer": [
                        {"coordinates": [262,477], "value": "X", "color": 0},
                ],
                "buyer_2_name_signer_title": [
                        {"coordinates": [503,478], "value": "X", "color": 0},
                ],
                "more_signers_checkbox": [
                        {"coordinates": [54,464], "value": "X", "color": 0},
                ],
                "seller_counter_offer_checkbox": [
                        {"coordinates": [72,386], "value": "X", "color": 0},
                ],
                "backup_offer_addendum_checkbox": [
                        {"coordinates": [72,373], "value": "X", "color": 0},
                ],
                "entity_sellers_checkbox": [
                        {"coordinates": [72,364], "value": "X", "color": 0},
                ],
                "entity_name_line_1": [
                        {"coordinates": [91,264], "value": "X", "color": 0},
                ],
                "entity_name_line_2": [
                        {"coordinates": [91,252], "value": "X", "color": 0},
                ],
                "entity_name_line_3": [
                        {"coordinates": [91,242], "value": "X", "color": 0},
                ],
                "seller_1_name": [
                        {"coordinates": [120,194], "value": "X", "color": 0},
                        {"coordinates": [180,182], "value": "X", "color": 0},
                        {"coordinates": [117,154], "value": "X", "color": 0},
                        {"coordinates": [179,142], "value": "X", "color": 0},
                ],
                "seller_1_name_signer_checkbox": [
                        {"coordinates": [72,167], "value": "X", "color": 0},
                        {"coordinates": [72,128], "value": "X", "color": 0},
                ],
                "seller_1_name_signer": [
                        {"coordinates": [260,167], "value": "X", "color": 0},
                        {"coordinates": [259,129], "value": "X", "color": 0},
                ],
                "seller_1_name_signer_title": [
                        {"coordinates": [503,167], "value": "X", "color": 0},
                        {"coordinates": [503,128], "value": "X", "color": 0},
                ],
                "more_sellers_checkbox": [
                        {"coordinates": [54,115], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [145,94], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [182,94], "value": "X", "color": 0},
                ],
                "not_accepted_date": [
                        {"coordinates": [496,94], "value": "X", "color": 0},
                ],
        },
        23:{
                "property_address": [
                        {"coordinates": [115,767], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [470,768], "value": "X", "color": 0},
                        {"coordinates": [492,597], "value": "X", "color": 0},
                        {"coordinates": [492,585], "value": "X", "color": 0},
                        {"coordinates": [492,478], "value": "X", "color": 0},
                        {"coordinates": [492,464], "value": "X", "color": 0},
                ],
                "buyer_brokerage_firm": [
                        {"coordinates": [176,609], "value": "X", "color": 0},
                ],
                "buyer_brokerage_number": [
                        {"coordinates": [473,610], "value": "X", "color": 0},
                ],
                "buyer_1_name": [
                        {"coordinates": [86,596], "value": "X", "color": 0},
                ],
                "buyer_1_number": [
                        {"coordinates": [379,598], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [88,584], "value": "X", "color": 0},
                ],
                "buyer_2_number": [
                        {"coordinates": [379,585], "value": "X", "color": 0},
                ],
                "buyer_address": [
                        {"coordinates": [107,571], "value": "X", "color": 0},
                ],
                "buyer_city": [
                        {"coordinates": [309,571], "value": "X", "color": 0},
                ],
                "buyer_state": [
                        {"coordinates": [474,571], "value": "X", "color": 0},
                ],
                "buyer_zip": [
                        {"coordinates": [514,571], "value": "X", "color": 0},
                ],
                "buyer_email": [
                        {"coordinates": [98,558], "value": "X", "color": 0},
                ],
                "buyer_phone": [
                        {"coordinates": [444,559], "value": "X", "color": 0},
                ],
                "more_agent_buyer_checkbox": [
                        {"coordinates": [72,546], "value": "X", "color": 0},
                ],
                "more_brokerage_buyer_checkbox": [
                        {"coordinates": [72,533], "value": "X", "color": 0},
                ],
                "email_above__buyer_checkbox": [
                        {"coordinates": [90,507], "value": "X", "color": 0},
                ],
                "text_to_phone_buyer_checkbox": [
                        {"coordinates": [155,507], "value": "X", "color": 0},
                ],
                "alternate_buyer_checkbox": [
                        {"coordinates": [261,507], "value": "X", "color": 0},
                ],
                "alternate_buyer_line": [
                        {"coordinates": [314,507], "value": "X", "color": 0},
                ],
                "seller_brokerage": [
                        {"coordinates": [171,489], "value": "X", "color": 0},
                ],
                "seller_brokerage_number": [
                        {"coordinates": [468,491], "value": "X", "color": 0},
                ],
                "seller_1_name": [
                        {"coordinates": [86,476], "value": "X", "color": 0},
                ],
                "seller_1_number": [
                        {"coordinates": [379,477], "value": "X", "color": 0},
                ],
                "seller_2_name": [
                        {"coordinates": [86,464], "value": "X", "color": 0},
                ],
                "seller_2_number": [
                        {"coordinates": [379,464], "value": "X", "color": 0},
                ],
                "seller_address": [
                        {"coordinates": [110,448], "value": "X", "color": 0},
                ],
                "seller_city": [
                        {"coordinates": [311,448], "value": "X", "color": 0},
                ],
                "seller_state": [
                        {"coordinates": [475,448], "value": "X", "color": 0},
                ],
                "seller_zip": [
                        {"coordinates": [512,448], "value": "X", "color": 0},
                ],
                "seller_email": [
                        {"coordinates": [101,434], "value": "X", "color": 0},
                ],
                "seller_phone": [
                        {"coordinates": [442,435], "value": "X", "color": 0},
                ],
                "more_agent_seller_checkbox": [
                        {"coordinates": [72,420], "value": "X", "color": 0},
                ],
                "more_brokerage_seller_checkbox": [
                        {"coordinates": [72,409], "value": "X", "color": 0},
                ],
                "email_above_seller_checkbox": [
                        {"coordinates": [90,383], "value": "X", "color": 0},
                ],
                "text_to_phone_seller_checkbox": [
                        {"coordinates": [155,383], "value": "X", "color": 0},
                ],
                "alternate_seller_checkbox": [
                        {"coordinates": [261,383], "value": "X", "color": 0},
                ],
                "alternate_seller_line": [
                        {"coordinates": [314,383], "value": "X", "color": 0},
                ],
                "escrew_holder_deposit_checkbox": [
                        {"coordinates": [352,338], "value": "X", "color": 0},
                ],
                "escrew_holder_deposit_amount": [
                        {"coordinates": [478,338], "value": "X", "color": 0},
                ],
                "counter_offer_number_1": [
                        {"coordinates": [98,329], "value": "X", "color": 0},
                ],
                "counter_offer_number_2": [
                        {"coordinates": [274,329], "value": "X", "color": 0},
                ],
                "escrow_holder_adviser": [
                        {"coordinates": [154,303], "value": "X", "color": 0},
                ],
                "escrew_holder_date_acceptance": [
                        {"coordinates": [514,304], "value": "X", "color": 0},
                ],
                "escrew_holder": [
                        {"coordinates": [100,291], "value": "X", "color": 0},
                ],
                "escrow_number": [
                        {"coordinates": [457,292], "value": "X", "color": 0},
                ],
                "escrow_by": [
                        {"coordinates": [52,278], "value": "X", "color": 0},
                ],
                "escrow_date": [
                        {"coordinates": [485,277], "value": "X", "color": 0},
                ],
                "escrow_address": [
                        {"coordinates": [72,265], "value": "X", "color": 0},
                ],
                "escrow_phone_fax_email": [
                        {"coordinates": [111,253], "value": "X", "color": 0},
                ],
                "escrow_holder_license": [
                        {"coordinates": [240,239], "value": "X", "color": 0},
                ],
                "financial_protection_checkbox": [
                        {"coordinates": [36,225], "value": "X", "color": 0},
                ],
                "insurance_checkbox": [
                        {"coordinates": [252,225], "value": "X", "color": 0},
                ],
                "real_estate_checkbox": [
                        {"coordinates": [366,225], "value": "X", "color": 0},
                ],
                "seller_initials_1": [
                        {"coordinates": [166,200], "value": "X", "color": 0},
                        {"coordinates": [496,163], "value": "X", "color": 0},
                ],
                "seller_initials_2": [
                        {"coordinates": [216,200], "value": "X", "color": 0},
                        {"coordinates": [543,163], "value": "X", "color": 0},
                ],
                "offer_date": [
                        {"coordinates": [485,200], "value": "X", "color": 0},
                ],
                "buyer_initials_1": [
                        {"coordinates": [333,163], "value": "X", "color": 0},
                ],
                "buyer_initials_2": [
                        {"coordinates": [378,163], "value": "X", "color": 0},
                ],
        },
        24:{
                "property_address": [
                        {"coordinates": [125,712], "value": "X", "color": 0},
                ],
        },
        25:{
                "buyer_1_name": [
                        {"coordinates": [75,592], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [485,592], "value": "X", "color": 0},
                        {"coordinates": [485,568], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [75,568], "value": "X", "color": 0},
                ],
        },
        26:{
                "purchase_agreement_other_checkbox": [
                        {"coordinates": [540,670], "value": "X", "color": 0},
                ],
                "purchase_agreement_other_line": [
                        {"coordinates": [40,658], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [70,645], "value": "X", "color": 0},
                        {"coordinates": [500,395], "value": "X", "color": 0},
                        {"coordinates": [500,365], "value": "X", "color": 0},
                        {"coordinates": [500,330], "value": "X", "color": 0},
                        {"coordinates": [500,300], "value": "X", "color": 0},
                ],
                "property_address": [
                        {"coordinates": [245,645], "value": "X", "color": 0},
                ],
                "seller1_seller2_name": [
                        {"coordinates": [90,632], "value": "X", "color": 0},
                ],
                "buyer_1_name": [
                        {"coordinates": [65,620], "value": "X", "color": 0},
                        {"coordinates": [80,395], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [80,365], "value": "X", "color": 0},
                ],
                "seller_1_name": [
                        {"coordinates": [80,330], "value": "X", "color": 0},
                ],
                "seller_2_name": [
                        {"coordinates": [80,300], "value": "X", "color": 0},
                ],
        },
        27:{
                "buyer_1_name": [
                        {"coordinates": [175,383], "value": "X", "color": 0},
                ],
                "date_prepared": [
                        {"coordinates": [490,383], "value": "X", "color": 0},
                        {"coordinates": [490,354], "value": "X", "color": 0},
                ],
                "buyer_2_name": [
                        {"coordinates": [175,354], "value": "X", "color": 0},
                ],
        },
}


def normalize_colors(colors):
    for i in range(0, len(colors)):
        for j in range(0, 3):
            colors[i][j] /= 255;

def main():
    reader = open("input.pdf", "rb");
    existing_pdf = PdfReader(reader)

    res = write_text(document_data, existing_pdf, reader);

def flatten(obj):

    out = [];

    keys = list(obj.keys());

    for i in range(0, len(keys)):
        coords = obj[keys[i]];

        for j in range(0, len(coords)):

            out.append(coords[j]);

    return out;

def write_text(document_data, input, reader):

    name = "output.pdf";

    keys = list(document_data.keys());

    for i in range(0, len(keys)):

        commands = flatten(document_data[keys[i]]);

        packet = io.BytesIO()
        packet.seek(0)
        can = canvas.Canvas(packet, pagesize=letter, bottomup=1);

        can.setFont("MainFont", font_size)

        if(len(commands) == 0): continue;

        for j in range(0, len(commands)):

            command = commands[j];
            coordinate = command['coordinates'];
            x = coordinate[0];
            y = coordinate[1];
            color = colors[command['color']];
            text = command['value'];
            can.setFillColorRGB(color[0], color[1], color[2]);

            can.drawString(x, y, text)

        can.save()

        new_pdf = PdfReader(packet)

        page = input.pages[i]
        page.merge_page(new_pdf.pages[0])

        print("Finished Page " + str(keys[i]))

    output = PdfWriter()

    for i in range(0, len(input.pages)):
        output.add_page(input.pages[i])

    reader.close();

    if(os.path.isfile(name)): os.remove(name);

    output_stream = open(name, "wb")

    print("Writing to '" + name + "'...");

    output.write(output_stream)
    output_stream.close()

    print("Finished writing!")

pdfmetrics.registerFont(TTFont('MainFont', font_file))
normalize_colors(colors);
main();
