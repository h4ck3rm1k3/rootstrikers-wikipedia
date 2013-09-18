# porting of fetch to python code borrowed from https://github.com/NYTimes/Fech
# wich is under the apache license
# https://github.com/NYTimes/Fech/blob/master/LICENSE
import re
import traceback 
#state enum
STATE_UNKNOWN = 0
STATE_HEADER = 1
STATE_BODY = 2

def dbg (x):
    traceback.print_stack(limit=2)
    print (x)

class Document:
    def __init__(self,url,filename):
        self.url=url
        self.filename=filename
        
class Header:
    def __init__(self,header,fec,version):
        self.header=header
        self.fec=fec
        self.version=version

class FileObject:
    def  __init__(self):
        self.attributes = {}


class Parser:

    def __init__(self):

        self.header=None

        self.filing_versions = ["8.0", "7.0", "6.4", "6.3", "6.2", "6.1",
                                  "5.3", "5.2", "5.1", "5.0", "3"]
        self.base_row_types = ["HDR", "F1", "F13", "F132", "F133", "F1M",
            "F2", "F24", "F3", "F3L", "F3P", "F3P31", "F3PS", "F3S", "F3X",
            "F4", "F5", "F56", "F57", "F6", "F65", "F7", "F76", "F9", "F91",
            "F92", "F93", "F94", "F99", "H1", "H2", "H3", "H4", "H5", "H6",
            "SchA", "SchB", "SchC", "SchC1", "SchC2", "SchD", "SchE", "SchF",
            "SchL", "TEXT"]
        ###
        # self.row_types_regex = {
        #     'hdr'   : r'^hdr$',
        #     'f1'    : r'^f1',
        #     'f13'   : r'^f13[an]',
        #     'f132'  : r'^f132',
        #     'f133'  : r'^f133',
        #     'f1m'   : r'(^f1m[^a|n])',
        #     'f2'    : r'(^f2$)|(^f2[^4])',
        #     'f24'   : r'(^f24$)|(^f24[an])',
        #     'f3'    : r'^f3[a|n|t]',
        #     'f3l'   : r'^f3l[a|n]',
        #     'f3p'   : r'(^f3p$)|(^f3p[^s|3])',
        #     'f3s'   : r'^f3s',
        #     'f3p31' : r'^f3p31',
        #     'f3ps'  : r'^f3ps',
        #     'f3x'   : r'(^f3x$)|(^f3x[ant])',
        #     'f4'    : r'^f4[na]',
        #     'f5'    : r'^f5[na]',
        #     'f56'   : r'^f56',
        #     'f57'   : r'^f57',
        #     'f6'    : r'(^f6$)|(^f6[an])',
        #     'f65'   : r'^f65',
        #     'f7'    : r'^f7[na]',
        #     'f76'   : r'^f76',
        #     'f9'    : r'^f9',
        #     'f91'   : r'^f91',
        #     'f92'   : r'^f92',
        #     'f93'   : r'^f93',
        #     'f94'   : r'^f94',
        #     'f99'   : r'^f99',
        #     'h1'    : r'^h1',
        #     'h2'    : r'^h2',
        #     'h3'    : r'^h3',
        #     'h4'    : r'^h4',
        #     'h5'    : r'^h5',
        #     'h6'    : r'^h6',
        #     'sa'    : r'^sa',
        #     'sb'    : r'^sb',
        #     'sc'    : r'^sc[^1-2]',
        #     'sc1'   : r'^sc1',
        #     'sc2'   : r'^sc2',
        #     'sd'    : r'^sd',
        #     'se'    : r'^se',
        #     'sf'    : r'^sf',
        #     'sl'    : r'^sl',
        #     'text'  : r'^text',
        # }

        self.row_types = {
            "HDR": self.row_type_hdr,
            "F1": self.row_type_f1,
            "F13": self.row_type_f13,
            "F132": self.row_type_f132,
            "F133": self.row_type_f133,
            "F1M": self.row_type_f1m,
            "F2": self.row_type_f2,
            "F24": self.row_type_f24,
            "F3": self.row_type_f3,
            "F3L": self.row_type_f3l,
            "F3P": self.row_type_f3p,
            "F3S": self.row_type_f3s,
            "F3P31": self.row_type_f3p31,
            "F3PS": self.row_type_f3ps,
            "F3X": self.row_type_f3x,
            "F4": self.row_type_f4,
            "F5": self.row_type_f5,
            "F56": self.row_type_f56,
            "F57": self.row_type_f57,
            "F6": self.row_type_f6,
            "F65": self.row_type_f65,
            "F7": self.row_type_f7,
            "F76": self.row_type_f76,
            "F9": self.row_type_f9,
            "F91": self.row_type_f91,
            "F92": self.row_type_f92,
            "F93": self.row_type_f93,
            "F94": self.row_type_f94,
            "F99": self.row_type_f99,
            "H1": self.row_type_h1,
            "H2": self.row_type_h2,
            "H3": self.row_type_h3,
            "H4": self.row_type_h4,
            "H5": self.row_type_h5,
            "H6": self.row_type_h6,
            "SchA": self.row_type_sa,
            "SchB": self.row_type_sb,
            "SchC": self.row_type_sc,
            "SchC1": self.row_type_sc1,
            "SchC2": self.row_type_sc2,
            "SchD": self.row_type_sd,
            "SchE": self.row_type_se,
            "SchF": self.row_type_sf,
            "SchL": self.row_type_sl,
            "TEXT": self.row_type_text,
        }

# Converts symbols and strings to Regexp objects for use in regex-keyed maps.
# Assumes that symbols should be matched literally, strings unanchored.
# @param [String,Symbol,Regexp] label the object to convert to a Regexp
    def regexify(self, label):
        if label in self.row_types_regex:
            return self.row_types[label]
        else:
            return r"^#{label.to_s}$"

    def row_type_hdr():
        pass

    def row_type_f1(self):
        pass

    def row_type_f13(self):
        pass

    def row_type_f132(self):
        pass

    def  row_type_f133(self):
        pass

    def row_type_f1m(self):
        pass

    def row_type_f2(self):
        pass

    def row_type_f24(self):
        pass

    def row_type_f3(self):
        pass

    def row_type_f3l(self):
        pass

    def row_type_f3p(self):
        pass

    def row_type_f3s(self):
        pass

    def row_type_f3p31(self):
        pass

    def row_type_f3ps(self):
        pass

    def row_type_f3x(self):
        pass

    def row_type_f4(self):
        pass

    def row_type_f5(self):
        pass

    def row_type_f56(self):
        pass

    def row_type_f57(self):
        pass

    def row_type_f6(self):
        pass

    def row_type_f65(self):
        pass

    def row_type_f7(self):
        pass

    def row_type_f76(self):
        pass

    def row_type_f9(self):
        pass

    def row_type_f91(self):
        pass

    def row_type_f92(self):
        pass

    def row_type_f93(self):
        pass

    def row_type_f94(self):
        pass

    def row_type_f99(self):
        pass

    def row_type_h1(self):
        pass

    def row_type_h2(self):
        pass

    def row_type_h3(self):
        pass

    def row_type_h4(self):
        pass

    def row_type_h5(self):
        pass

    def row_type_h6(self):
        pass

    def row_type_sa(self):
        pass

    def row_type_sb(self):
        pass

    def row_type_sc(self):
        pass

    def row_type_sc1(self):
        pass

    def row_type_sc2(self):
        pass

    def row_type_sd(self):
        pass

    def row_type_se(self):
        pass

    def row_type_sf(self):
        pass

    def row_type_sl(self):
        pass

    def row_type_text(self):
        pass

    def field_11_a_iii_individuals_total(self):
        pass

    def field_11_a_ii_individuals_unitemized(self):
        pass

    def field_11_a_i_individuals_itemized(self):
        pass

    def field_11_b_political_party_committees(self):
        pass

    def field_11_c_all_other_political_committees_pacs(self):
        pass

    def field_11_d_the_candidate(self):
        pass

    def field_11_e_total_contributions(self):
        pass

    def field_12_transfers_from_other_auth_committees(self):
        pass

    def field_13_a_loans_made_or_guarn_by_the_candidate(self):
        pass

    def field_13_b_all_other_loans(self):
        pass

    def field_13_c_total_loans(self):
        pass

    def field_14_net_contributions(self):
        pass

    def field_14_offsets_to_operating_expenditures(self):
        pass

    def field_15_net_expenditures(self):
        pass

    def field_15_other_receipts(self):
        pass

    def field_16_federal_funds(self):
        pass

    def field_16_total_receipts(self):
        pass

    def field_17_a_iii_individual_contribution_total(self):
        pass

    def field_17_a_ii_individuals_unitemized(self):
        pass

    def field_17_a_i_individuals_itemized(self):
        pass

    def field_17_a_individuals(self):
        pass

    def field_17_b_political_party_committees(self):
        pass

    def field_17_c_other_political_committees_pacs(self):
        pass

    def field_17_d_the_candidate(self):
        pass

    def field_17_e_total_contributions_other_than_loans(self):
        pass

    def field_17_operating_expenditures(self):
        pass

    def field_18_transfers_from_aff_other_party_committees(self):
        pass

    def field_18_transfers_to_other_auth_committees(self):
        pass

    def field_19_a_loan_repayment_by_candidate(self):
        pass

    def field_19_a_received_from_or_guaranteed_by_candidate(self):
        pass

    def field_19_b_loan_repayments_all_other_loans(self):
        pass

    def field_19_b_other_loans(self):
        pass

    def field_19_c_total_loan_repayments(self):
        pass

    def field_19_c_total_loans(self):
        pass

    def field_20_a_operating(self):
        pass

    def field_20_a_refund_individuals_other_than_pol_cmtes(self):
        pass

    def field_20_b_fundraising(self):
        pass

    def field_20_b_refund_political_party_committees(self):
        pass

    def field_20_c_legal_and_accounting(self):
        pass

    def field_20_c_refund_other_political_committees(self):
        pass

    def field_20_d_total_contributions_refunds(self):
        pass

    def field_20_d_total_offsets_to_operating_expenditures(self):
        pass

    def field_21_other_disbursements(self):
        pass

    def field_21_other_receipts(self):
        pass

    def field_22_total_disbursements(self):
        pass

    def field_22_total_receipts(self):
        pass

    def field_23_operating_expenditures(self):
        pass

    def field_24_transfers_to_other_authorized_committees(self):
        pass

    def field_25_fundraising_disbursements(self):
        pass

    def field_26_exempt_legal_and_accounting_disbursements(self):
        pass

    def field_27_a_made_or_guaranteed_by_the_candidate(self):
        pass

    def field_27_b_other_repayments(self):
        pass

    def field_27_c_total_loan_repayments_made(self):
        pass

    def field_28_a_individuals(self):
        pass

    def field_28_b_political_party_committees(self):
        pass

    def field_28_c_other_political_committees(self):
        pass

    def field_28_d_total_contributions_refunds(self):
        pass

    def field_29_other_disbursements(self):
        pass

    def field_30(self):
        pass

    def field_30_total_disbursements(self):
        pass

    def field_6a_total_contributions_no_loans(self):
        pass

    def field_6b_total_contribution_refunds(self):
        pass

    def field_6c_net_contributions(self):
        pass

    def field_7a_total_operating_expenditures(self):
        pass

    def field_7b_total_offsets_to_operating_expenditures(self):
        pass

    def field_7c_net_operating_expenditures(self):
        pass

    def field_account_identifier(self):
        pass

    def field_account_location_name(self):
        pass

    def field_account_name(self):
        pass

    def field_activity_event_name(self):
        pass

    def field_activity_general(self):
        pass

    def field_activity(self): #ACTIVITY
        pass

    def field_activity_primary(self):
        pass

    def field_actual_direct_candidate_support_federal(self):
        pass

    def field_actual_direct_candidate_support_federal_percent(self):
        pass

    def field_actual_direct_candidate_support_nonfederal(self):
        pass

    def field_added(self):
        pass

    def field_administrative_ratio_applies(self):
        pass

    def field_administrative_voter_drive_activity(self):
        pass

    def field_affiliated_candidate_id_number(self):
        pass

    def field_affiliated_city(self):
        pass

    def field_affiliated_committee_id_number(self):
        pass

    def field_affiliated_committee_name(self):
        pass

    def field_affiliated_date_f1_filed(self):
        pass

    def field_affiliated_first_name(self):
        pass

    def field_affiliated_last_name(self):
        pass

    def field_affiliated_middle_name(self):
        pass

    def field_affiliated_prefix(self):
        pass

    def field_affiliated_relationship_code(self):
        pass

    def field_affiliated_state(self):
        pass

    def field_affiliated_street_1(self):
        pass

    def field_affiliated_street_2(self):
        pass

    def field_affiliated_suffix(self):
        pass

    def field_affiliated_zip_code(self):
        pass

    def field_agent_city(self):
        pass

    def field_agent_first_name(self):
        pass

    def field_agent_last_name(self):
        pass

    def field_agent_middle_name(self):
        pass

    def field_agent_name(self):
        pass

    def field_agent_prefix(self):
        pass

    def field_agent_state(self):
        pass

    def field_agent_street_1(self):
        pass

    def field_agent_street_2(self):
        pass

    def field_agent_suffix(self):
        pass

    def field_agent_telephone(self):
        pass

    def field_agent_title(self):
        pass

    def field_agent_zip_code(self):
        pass

    def field_aggregate_general_elec_expended(self):
        pass

    def field_a_iii_individual_contribution_total(self):
        pass

    def field_a_iii_individuals_total(self):
        pass

    def field_a_ii_individuals_unitemized(self):
        pass

    def field_a_i_individuals_itemized(self):
        pass

    def field_a_individuals(self):
        pass

    def field_alabama(self):
        pass

    def field_alaska(self):
        pass

    def field_a_loan_repayment_by_candidate(self):
        pass

    def field_a_loans_made_or_guarn_by_the_candidate(self):
        pass

    def field_a_made_or_guaranteed_by_the_candidate(self):
        pass

    def field_amended_cd(self):
        pass

    def field_amended_code(self):
        pass

    def field_amendment_date(self):
        pass

    def field_a_operating(self):
        pass

    def field_A(self):
        pass

    def field_a_received_from_or_guaranteed_by_candidate(self):
        pass

    def field_a_refund_individuals_other_than_pol_cmtes(self):
        pass

    def field_arizona(self):
        pass

    def field_arkansas(self):
        pass

    def field_a_total_contributions_no_loans(self):
        pass

    def field_a_total_operating_expenditures(self):
        pass

    def field_at(self):
        pass

    def field_authorized_committee_city(self):
        pass

    def field_authorized_committee_id_number(self):
        pass

    def field_authorized_committee_name(self):
        pass

    def field_authorized_committee_state(self):
        pass

    def field_authorized_committee_street_1(self):
        pass

    def field_authorized_committee_street_2(self):
        pass

    def field_authorized_committee_zip_code(self):
        pass

    def field_authorized_first_name(self):
        pass

    def field_authorized_last_name(self):
        pass

    def field_authorized_middle_name(self):
        pass

    def field_authorized_name(self):
        pass

    def field_authorized_prefix(self):
        pass

    def field_authorized_suffix(self):
        pass

    def field_authorized_title(self):
        pass

    def field_back_reference_sched_form_name(self):
        pass

    def field_back_reference_sched_name(self):
        pass

    def field_back_reference_tran_id_number(self):
        pass

    def field_balance_at_close_this_period(self):
        pass

    def field_ballot_governor(self):
        pass

    def field_b_all_other_loans(self):
        pass

    def field_ballot_house(self):
        pass

    def field_ballot_local_candidates(self):
        pass

    def field_ballot_other_statewide(self):
        pass

    def field_ballot_presidential(self):
        pass

    def field_ballot_senate(self):
        pass

    def field_ballot_state_representative(self):
        pass

    def field_ballot_state_senate(self):
        pass

    def field_bank2_city(self):
        pass

    def field_bank2_name(self):
        pass

    def field_bank2_state(self):
        pass

    def field_bank2_street_1(self):
        pass

    def field_bank2_street_2(self):
        pass

    def field_bank2_zip_code(self):
        pass

    def field_bank_city(self):
        pass

    def field_bank_name(self):
        pass

    def field_bank_state(self):
        pass

    def field_bank_street_1(self):
        pass

    def field_bank_street_2(self):
        pass

    def field_bank_zip_code(self):
        pass

    def field_beginning_balance_this_period(self):
        pass

    def field_beneficiary_candidate_district(self):
        pass

    def field_beneficiary_candidate_fec_id(self):
        pass

    def field_beneficiary_candidate_first_name(self):
        pass

    def field_beneficiary_candidate_last_name(self):
        pass

    def field_beneficiary_candidate_middle_name(self):
        pass

    def field_beneficiary_candidate_name(self):
        pass

    def field_beneficiary_candidate_office(self):
        pass

    def field_beneficiary_candidate_prefix(self):
        pass

    def field_beneficiary_candidate_state(self):
        pass

    def field_beneficiary_candidate_suffix(self):
        pass

    def field_beneficiary_committee_fec_id(self):
        pass

    def field_beneficiary_committee_name(self):
        pass

    def field_b_fundraising(self):
        pass

    def field_b_loan_repayments_all_other_loans(self):
        pass

    def field_b_other_loans(self):
        pass

    def field_b_other_repayments(self):
        pass

    def field_B(self):
        pass

    def field_b_political_party_committees(self):
        pass

    def field_b_refund_political_party_committees(self):
        pass

    def field_b_total_contribution_refunds(self):
        pass

    def field_b_total_offsets_to_operating_expenditures(self):
        pass
#    def field_Bundled}"(self):
        pass

    def field_calendar_y_t_d_per_election_office(self):
        pass

    def field_california(self):
        pass

    def field_c_all_other_political_committees_pacs(self):
        pass

    def field_candidate_city(self):
        pass

    def field_candidate_district(self):
        pass

    def field_candidate_first_name(self):
        pass

    def field_candidate_id_number(self):
        pass

    def field_candidate_id(self):
        pass

    def field_candidate_last_name(self):
        pass

    def field_candidate_middle_name(self):
        pass

    def field_candidate_name(self):
        pass

    def field_candidate_office(self):
        pass

    def field_candidate_party_code(self):
        pass

    def field_candidate_prefix(self):
        pass

    def field_candidate_signature_first_name(self):
        pass

    def field_candidate_signature_last_name(self):
        pass

    def field_candidate_signature_middle_name(self):
        pass

    def field_candidate_signature_name(self):
        pass

    def field_candidate_signature_prefix(self):
        pass

    def field_candidate_signature_suffix(self):
        pass

    def field_candidate_state(self):
        pass

    def field_candidate_street_1(self):
        pass

    def field_candidate_street_2(self):
        pass

    def field_candidate_suffix(self):
        pass

    def field_candidate_zip_code(self):
        pass

    def field_canonical(self):
        pass

    def field_category_code(self):
        pass

    def field_change_of_address(self):
        pass

    def field_change_of_committee_email(self):
        pass

    def field_change_of_committee_name(self):
        pass

    def field_change_of_committee_url(self):
        pass

    def field_city(self):
        pass

    def field_c_legal_and_accounting(self):
        pass

    def field_c_net_contributions(self):
        pass

    def field_c_net_operating_expenditures(self):
        pass

    def field_col_a_alabama(self):
        pass

    def field_col_a_alaska(self):
        pass

    def field_col_a_arizona(self):
        pass

    def field_col_a_arkansas(self):
        pass

    def field_col_a_california(self):
        pass

    def field_col_a_candidate_contributions(self):
        pass

    def field_col_a_candidate_loan_repayments(self):
        pass

    def field_col_a_candidate_loans(self):
        pass

    def field_col_a_cash_beginning_reporting_period(self):
        pass

    def field_col_a_cash_on_hand_beginning_period(self):
        pass

    def field_col_a_cash_on_hand_beginning_reporting_period(self):
        pass

    def field_col_a_cash_on_hand_close_of_period(self):
        pass

    def field_col_a_cash_on_hand_close(self):
        pass

    def field_col_a_colorado(self):
        pass

    def field_col_a_connecticut(self):
        pass

    def field_col_a_contributions_itemized(self):
        pass

    def field_col_a_contributions_subtotal(self):
        pass

    def field_col_a_contributions_to_candidates(self):
        pass

    def field_col_a_contributions_unitemized(self):
        pass

    def field_col_a_convention_expenditures(self):
        pass

    def field_col_a_convention_expenses_itemized(self):
        pass

    def field_col_a_convention_expenses_subtotal(self):
        pass

    def field_col_a_convention_expenses_unitemized(self):
        pass

    def field_col_a_convention_refunds_itemized(self):
        pass

    def field_col_a_convention_refunds(self):
        pass

    def field_col_a_convention_refunds_subtotal(self):
        pass

    def field_col_a_convention_refunds_unitemized(self):
        pass

    def field_col_a_coordinated_expenditures_by_party_committees(self):
        pass

    def field_col_a_debts_by(self):
        pass

    def field_col_a_debts_to(self):
        pass

    def field_col_a_delaware(self):
        pass

    def field_col_a_disbursements_subtotal(self):
        pass

    def field_col_a_dist_of_columbia(self):
        pass

    def field_col_a_exempt_legal_accounting_disbursement(self):
        pass

    def field_col_a_expenditures_subject_to_limits(self):
        pass

    def field_col_a_federal_election_activity_all_federal(self):
        pass

    def field_col_a_federal_election_activity_federal_share(self):
        pass

    def field_col_a_federal_election_activity_levin_share(self):
        pass

    def field_col_a_federal_election_activity_total(self):
        pass

    def field_col_a_federal_funds(self):
        pass

    def field_col_a_florida(self):
        pass

    def field_col_a_fundraising_disbursements(self):
        pass

    def field_col_a_fundraising(self):
        pass

    def field_col_a_generic_campaign_disbursements(self):
        pass

    def field_col_a_georgia(self):
        pass

    def field_col_a_gotv_disbursements(self):
        pass

    def field_col_a_guam(self):
        pass

    def field_col_a_hawaii(self):
        pass

    def field_col_a_idaho(self):
        pass

    def field_col_a_illinois(self):
        pass

    def field_col_a_independent_expenditures(self):
        pass

    def field_col_a_indiana(self):
        pass

    def field_col_a_individual_contributions_itemized(self):
        pass


    def field_col_a_individual_contributions_unitemized(self):
        pass

    def field_col_a_individual_contribution_total(self):
        pass

    def field_col_a_individuals_itemized(self):
        pass

    def field_col_a_individuals(self):
        pass

    def field_col_a_individuals_unitemized(self):
        pass

    def field_col_a_iowa(self):
        pass

    def field_col_a_itemized_receipts_persons(self):
        pass

    def field_col_a_items_on_hand_to_be_liquidated(self):
        pass

    def field_col_a_kansas(self):
        pass

    def field_col_a_kentucky(self):
        pass

    def field_col_a_legal_and_accounting(self):
        pass

    def field_col_a_levin_funds(self):
        pass

    def field_col_a_loan_disbursements_subtotal(self):
        pass

    def field_col_a_loan_receipts_subtotal(self):
        pass

    def field_col_a_loan_repayments_made(self):
        pass

    def field_col_a_loan_repayments_received(self):
        pass

    def field_col_a_loans_made(self):
        pass

    def field_col_a_loans_received(self):
        pass

    def field_col_a_louisiana(self):
        pass

    def field_col_a_made_or_guaranteed_by_candidate(self):
        pass

    def field_col_a_maine(self):
        pass

    def field_col_a_maryland(self):
        pass

    def field_col_a_massachusetts(self):
        pass

    def field_col_a_michigan(self):
        pass

    def field_col_a_minnesota(self):
        pass

    def field_col_a_mississippi(self):
        pass

    def field_col_a_missouri(self):
        pass

    def field_col_a_montana(self):
        pass

    def field_col_a_nebraska(self):
        pass

    def field_col_a_net_contributions(self):
        pass

    def field_col_a_net_operating_expenditures(self):
        pass

    def field_col_a_nevada(self):
        pass

    def field_col_a_new_hampshire(self):
        pass

    def field_col_a_new_jersey(self):
        pass

    def field_col_a_new_mexico(self):
        pass

    def field_col_a_new_york(self):
        pass

    def field_col_a_north_carolina(self):
        pass

    def field_col_a_north_dakota(self):
        pass

    def field_col_a_offsets_to_expenditures(self):
        pass

    def field_col_a_offset_to_operating_expenditures(self):
        pass

    def field_col_a_ohio(self):
        pass

    def field_col_a_oklahoma(self):
        pass

    def field_col_a_operating_expenditures(self):
        pass

    def field_col_a_operating(self):
        pass

    def field_col_a_oregon(self):
        pass

    def field_col_a_other_disbursements_itemized(self):
        pass

    def field_col_a_other_disbursements(self):
        pass

    def field_col_a_other_disbursements_subtotal(self):
        pass

    def field_col_a_other_disbursements_unitemized(self):
        pass

    def field_col_a_other_federal_operating_expenditures(self):
        pass

    def field_col_a_other_federal_receipts(self):
        pass

    def field_col_a_other_income_itemized(self):
        pass

    def field_col_a_other_income_subtotal(self):
        pass

    def field_col_a_other_income_unitemized(self):
        pass

    def field_col_a_other_loan_repayments(self):
        pass

    def field_col_a_other_loans(self):
        pass

    def field_col_a_other_political_committees_pacs(self):
        pass

    def field_col_a_other_political_committees(self):
        pass

    def field_col_a_other_receipts(self):
        pass

    def field_col_a_other_refunds_itemized(self):
        pass

    def field_col_a_other_refunds_subtotal(self):
        pass

    def field_col_a_other_refunds_unitemized(self):
        pass

    def field_col_a_other_repayments(self):
        pass

    def field_col_a_pac_contributions(self):
        pass

    def field_col_a_pennsylvania(self):
        pass

    def field_text(self):
        pass

    def field_nonfederal_percentage(self):
        pass

    def field_rec_type(self):
        pass

    def field_col_b_gross_receipts_minus_personal_funds_general(self):
        pass

    def field_col_a_political_party_committees(self):
        pass

    def field_col_a_political_party_committees_receipts(self):
        pass

    def field_col_a_political_party_committees_refunds(self):
        pass

    def field_col_a_political_party_contributions(self):
        pass    

    def field_col_a_prior_expenditures_subject_to_limits(self):
        pass

    def field_col_a_puerto_rico(self):
        pass

    def field_col_a_receipts_period(self):
        pass

    def field_col_a_received_from_or_guaranteed_by_cand(self):
        pass

    def field_col_a_refunds_to_individuals(self):
        pass

    def field_col_a_refunds_to_other_committees(self):
        pass

    def field_col_a_refunds_to_party_committees(self):
        pass

    def field_col_a_rhode_island(self):
        pass

    def field_col_a_shared_operating_expenditures_federal(self):
        pass

    def field_col_a_shared_operating_expenditures_nonfederal(self):
        pass

    def field_col_a_south_carolina(self):
        pass

    def field_col_a_south_dakota(self):
        pass

    def field_col_a_subtotal(self):
        pass

    def field_col_a_subtotal_period(self):
        pass

    def field_col_a_tennessee(self):
        pass

    def field_col_a_texas(self):
        pass

    def field_col_a_the_candidate(self):
        pass

    def field_col_a_total_contributions_no_loans(self):
        pass

    def field_col_a_total_contributions(self):
        pass

    def field_col_a_total_contributions_refunds(self):
        pass

    def field_col_a_total_disbursements(self):
        pass

    def field_col_a_total_expenditures_subject_to_limits(self):
        pass

    def field_col_a_total_federal_disbursements(self):
        pass

    def field_col_a_total_federal_operating_expenditures(self):
        pass

    def field_col_a_total_federal_receipts(self):
        pass

    def field_col_a_total_individual_contributions(self):
        pass

    def field_col_a_total_loan_repayments_made(self):
        pass

    def field_col_a_total_loan_repayments(self):
        pass

    def field_col_a_total_loan_repayments_received(self):
        pass

    def field_col_a_total_loans(self):
        pass

    def field_col_a_total_nonfederal_transfers(self):
        pass

    def field_col_a_total_offsets_to_expenditures(self):
        pass

    def field_col_a_total_offsets_to_operating_expenditures(self):
        pass

    def field_col_a_total_offset_to_operating_expenditures(self):
        pass

    def field_col_a_total_operating_expenditures(self):
        pass

    def field_col_a_total_receipts(self):
        pass

    def field_col_a_total_receipts_period(self):
        pass

    def field_col_a_total_receipts_persons(self):
        pass

    def field_col_a_total_refunds(self):
        pass

    def field_col_a_totals(self):
        pass

    def field_col_a_transfers_from_aff_other_party_cmttees(self):
        pass

    def field_col_a_transfers_from_authorized(self):
        pass

    def field_col_a_transfers_from_nonfederal_h3(self):
        pass

    def field_col_a_transfers_to_affiliated(self):
        pass

    def field_col_a_transfers_to_authorized(self):
        pass

    def field_col_a_transfers_to_other_authorized_committees(self):
        pass

    def field_col_a_unitemized_receipts_persons(self):
        pass

    def field_col_a_utah(self):
        pass

    def field_col_a_vermont(self):
        pass

    def field_col_a_virginia(self):
        pass

    def field_col_a_virgin_islands(self):
        pass

    def field_col_a_voter_id_disbursements(self):
        pass

    def field_col_a_voter_registration_disbursements(self):
        pass

    def field_col_a_washington(self):
        pass

    def field_col_a_west_virginia(self):
        pass

    def field_col_a_wisconsin(self):
        pass

    def field_col_a_wyoming(self):
        pass

    def field_col_b_aggregate_personal_funds_general(self):
        pass

    def field_col_b_aggregate_personal_funds_primary(self):
        pass

    def field_col_b_alabama(self):
        pass

    def field_col_b_alaska(self):
        pass

    def field_col_b_arizona(self):
        pass

    def field_col_b_arkansas(self):
        pass

    def field_col_b_beginning_year(self):
        pass

    def field_col_b_california(self):
        pass

    def field_col_b_candidate_contributions(self):
        pass

    def field_col_b_candidate_loan_repayments(self):
        pass

    def field_col_b_candidate_loans(self):
        pass

    def field_col_b_cash_on_hand_beginning_period(self):
        pass

    def field_col_b_cash_on_hand_beginning_year(self):
        pass

    def field_col_b_cash_on_hand_close_of_period(self):
        pass

    def field_col_b_cash_on_hand_jan_1(self):
        pass

    def field_col_b_colorado(self):
        pass

    def field_col_b_connecticut(self):
        pass

    def field_col_b_contributions_subtotal(self):
        pass

    def field_col_b_contributions_to_candidates(self):
        pass

    def field_col_b_convention_expenditures(self):
        pass

    def field_col_b_convention_expenses_subtotal(self):
        pass

    def field_col_b_convention_refunds(self):
        pass

    def field_col_b_convention_refunds_subtotal(self):
        pass

    def field_col_b_coordinated_expenditures_by_party_committees(self):
        pass

    def field_col_b_delaware(self):
        pass

    def field_col_b_disbursements_period(self):
        pass

    def field_col_b_disbursements_subtotal(self):
        pass

    def field_col_b_dist_of_columbia(self):
        pass

    def field_col_b_exempt_legal_accounting_disbursement(self):
        pass

    def field_col_b_expenditures_subject_to_limits(self):
        pass

    def field_col_b_federal_election_activity_all_federal(self):
        pass

    def field_col_b_federal_election_activity_federal_share(self):
        pass

    def field_col_b_federal_election_activity_levin_share(self):
        pass

    def field_col_b_federal_election_activity_total(self):
        pass

    def field_col_b_federal_funds(self):
        pass

    def field_col_b_florida(self):
        pass

    def field_col_b_fundraising_disbursements(self):
        pass

    def field_col_b_fundraising(self):
        pass

    def field_col_b_generic_campaign_disbursements(self):
        pass

    def field_col_b_georgia(self):
        pass

    def field_col_b_gotv_disbursements(self):
        pass

    def field_col_b_gross_receipts_authorized_general(self):
        pass

    def field_col_b_gross_receipts_authorized_primary(self):
        pass

    def field_col_b_gross_receipts_minus_personal_funds_primary(self):
        pass

    def field_col_b_guam(self):
        pass

    def field_col_b_hawaii(self):
        pass

    def field_col_b_idaho(self):
        pass

    def field_col_b_illinois(self):
        pass

    def field_col_b_independent_expenditures(self):
        pass

    def field_col_b_indiana(self):
        pass

    def field_col_b_individual_contributions_itemized(self):
        pass

    def field_col_b_individual_contributions_unitemized(self):
        pass

    def field_col_b_individual_contribution_total(self):
        pass

    def field_col_b_individuals_itemized(self):
        pass

    def field_col_b_individuals(self):
        pass

    def field_col_b_individuals_unitemized(self):
        pass

    def field_col_b_iowa(self):
        pass

    def field_col_b_itemized_receipts_persons(self):
        pass

    def field_col_b_kansas(self):
        pass

    def field_col_b_kentucky(self):
        pass

    def field_col_b_legal_and_accounting(self):
        pass

    def field_col_b_levin_funds(self):
        pass

    def field_col_b_loan_disbursements_subtotal(self):
        pass

    def field_col_b_loan_receipts_subtotal(self):
        pass

    def field_col_b_loans_made(self):
        pass

    def field_col_b_louisiana(self):
        pass

    def field_col_b_made_or_guaranteed_by_the_candidate(self):
        pass

    def field_col_b_maine(self):
        pass

    def field_col_b_maryland(self):
        pass

    def field_col_b_massachusetts(self):
        pass

    def field_col_b_michigan(self):
        pass

    def field_col_b_minnesota(self):
        pass

    def field_col_b_mississippi(self):
        pass

    def field_col_b_missouri(self):
        pass

    def field_col_b_montana(self):
        pass

    def field_col_b_nebraska(self):
        pass

    def field_col_b_net_contributions(self):
        pass

    def field_col_b_net_operating_expenditures(self):
        pass

    def field_col_b_nevada(self):
        pass

    def field_col_b_new_hampshire(self):
        pass

    def field_col_b_new_jersey(self):
        pass

    def field_col_b_new_mexico(self):
        pass

    def field_col_b_new_york(self):
        pass

    def field_col_b_north_carolina(self):
        pass

    def field_col_b_north_dakota(self):
        pass

    def field_col_b_offsets_to_expenditures(self):
        pass

    def field_col_b_offset_to_operating_expenditures(self):
        pass

    def field_col_b_ohio(self):
        pass

    def field_col_b_oklahoma(self):
        pass

    def field_col_b_operating_expenditures(self):
        pass

    def field_col_b_operating(self):
        pass

    def field_col_b_oregon(self):
        pass

    def field_col_b_other_disbursements(self):
        pass

    def field_col_b_other_disbursements_subtotal(self):
        pass

    def field_col_b_other_federal_operating_expenditures(self):
        pass

    def field_col_b_other_federal_receipts(self):
        pass

    def field_col_b_other_income_subtotal(self):
        pass

    def field_col_b_other_loan_repayments(self):
        pass

    def field_col_b_other_loans(self):
        pass

    def field_col_b_other_political_committees_pacs(self):
        pass

    def field_col_b_other_political_committees(self):
        pass

    def field_col_b_other_receipts(self):
        pass

    def field_col_b_other_refunds_subtotal(self):
        pass

    def field_col_b_other_repayments(self):
        pass

    def field_col_b_pac_contributions(self):
        pass

    def field_col_b_pennsylvania(self):
        pass

    def field_col_b_political_party_committees(self):
        pass

    def field_col_b_political_party_committees_receipts(self):
        pass

    def field_col_b_political_party_committees_refunds(self):
        pass

    def field_col_b_political_party_contributions(self):
        pass

    def field_col_b_prior_expendiutres_subject_to_limits(self):
        pass

    def field_col_b_puerto_rico(self):
        pass

    def field_col_b_receipts_period(self):
        pass

    def field_col_b_received_from_or_guaranteed_by_cand(self):
        pass

    def field_col_b_refunds_to_individuals(self):
        pass

    def field_col_b_refunds_to_other_committees(self):
        pass

    def field_col_b_refunds_to_party_committees(self):
        pass

    def field_col_b_rhode_island(self):
        pass

    def field_col_b_shared_operating_expenditures_federal(self):
        pass

    def field_col_b_shared_operating_expenditures_nonfederal(self):
        pass

    def field_col_b_south_carolina(self):
        pass

    def field_col_b_south_dakota(self):
        pass

    def field_col_b_subtotal(self):
        pass

    def field_col_b_subtotal_period(self):
        pass

    def field_col_b_tennessee(self):
        pass

    def field_col_b_texas(self):
        pass

    def field_col_b_the_candidate(self):
        pass

    def field_col_b_total_contributions_no_loans(self):
        pass

    def field_col_b_total_contributions_other_than_loans(self):
        pass

    def field_col_b_total_contributions(self):
        pass

    def field_col_b_total_contributions_refunds(self):
        pass

    def field_col_b_total_disbursements(self):
        pass

    def field_col_b_total_expenditures_subject_to_limits(self):
        pass

    def field_col_b_total_federal_disbursements(self):
        pass

    def field_col_b_total_federal_operating_expenditures(self):
        pass

    def field_col_b_total_federal_receipts(self):
        pass

    def field_col_b_total_individual_contributions(self):
        pass

    def field_col_b_total_loan_repayments_made(self):
        pass

    def field_col_b_total_loan_repayments(self):
        pass

    def field_col_b_total_loan_repayments_received(self):
        pass

    def field_col_b_total_loans(self):
        pass

    def field_col_b_total_nonfederal_transfers(self):
        pass

    def field_col_b_total_offsets_to_expenditures(self):
        pass

    def field_col_b_total_offsets_to_operating_expenditures(self):
        pass

    def field_col_b_total_offset_to_operating_expenditures(self):
        pass

    def field_col_b_total_operating_expenditures(self):
        pass

    def field_col_b_total_receipts(self):
        pass

    def field_col_b_total_receipts_persons(self):
        pass

    def field_col_b_total_refunds(self):
        pass

    def field_col_b_totals(self):
        pass

    def field_col_b_transfers_from_affiliated(self):
        pass

    def field_col_b_transfers_from_aff_other_party_cmttees(self):
        pass

    def field_col_b_transfers_from_authorized(self):
        pass

    def field_col_b_transfers_from_nonfederal_h3(self):
        pass

    def field_col_b_transfers_to_affiliated(self):
        pass

    def field_col_b_transfers_to_authorized(self):
        pass

    def field_col_b_transfers_to_other_authorized_committees(self):
        pass

    def field_col_b_unitemized_receipts_persons(self):
        pass

    def field_col_b_utah(self):
        pass

    def field_col_b_vermont(self):
        pass

    def field_col_b_virginia(self):
        pass

    def field_col_b_virgin_islands(self):
        pass

    def field_col_b_voter_id_disbursements(self):
        pass

    def field_col_b_voter_registration_disbursements(self):
        pass

    def field_col_b_washington(self):
        pass

    def field_col_b_west_virginia(self):
        pass

    def field_col_b_wisconsin(self):
        pass

    def field_col_b_wyoming(self):
        pass

    def field_col_b_year(self):
        pass

    def field_collateral(self):
        pass

    def field_collateral_value_amount(self):
        pass

    def field_colorado(self):
        pass

    def field_COLUMN(self):
        pass

    def field_comment(self):
        pass

    def field_committee_city(self):
        pass

    def field_committee_email(self):
        pass

    def field_committee_fax_number(self):
        pass

    def field_committee_id_number(self):
        pass

    def field_committee_name(self):
        pass

    def field_committee_state(self):
        pass

    def field_committee_street_1(self):
        pass

    def field_committee_street_2(self):
        pass

    def field_committee_type_description(self):
        pass

    def field_committee_type(self):
        pass

    def field_committee_url(self):
        pass

    def field_committee_zip_code(self):
        pass

    def field_communication_class(self):
        pass

    def field_communication_cost(self):
        pass

    def field_communication_date(self):
        pass

    def field_communication_title(self):
        pass

    def field_communication_type_description(self):
        pass

    def field_communication_type(self):
        pass

    def field_completing_first_name(self):
        pass

    def field_completing_last_name(self):
        pass

    def field_completing_middle_name(self):
        pass

    def field_completing_prefix(self):
        pass

    def field_completing_suffix(self):
        pass

    def field_conduit_city(self):
        pass

    def field_conduit_committee_id(self):
        pass

    def field_conduit_name(self):
        pass

    def field_conduit_state(self):
        pass

    def field_conduit_street_1(self):
        pass

    def field_conduit_street1(self):
        pass

    def field_conduit_street_2(self):
        pass

    def field_conduit_street2(self):
        pass

    def field_conduit_zip_code(self):
        pass

    def field_connecticut(self):
        pass

    def field_contribution_aggregate(self):
        pass

    def field_contribution_amount(self):
        pass

    def field_contribution_date(self):
        pass

    def field_contribution_purpose_code(self):
        pass

    def field_contribution_purpose_descrip(self):
        pass

    def field_contributor_city(self):
        pass

    def field_contributor_employer(self):
        pass

    def field_contributor_fec_id(self):
        pass

    def field_contributor_first_name(self):
        pass

    def field_contributor_last_name(self):
        pass

    def field_contributor_middle_name(self):
        pass

    def field_contributor_name(self):
        pass

    def field_contributor_occupation(self):
        pass

    def field_contributor_organization_name(self):
        pass

    def field_contributor_prefix(self):
        pass

    def field_contributor_state(self):
        pass

    def field_contributor_street_1(self):
        pass

    def field_contributor_street_2(self):
        pass

    def field_contributor_suffix(self):
        pass

    def field_contributor_zip_code(self):
        pass

    def field_contributor_zip(self):
        pass

    def field_controller_city(self):
        pass

    def field_controller_employer(self):
        pass

    def field_controller_first_name(self):
        pass

    def field_controller_last_name(self):
        pass

    def field_controller_middle_name(self):
        pass

    def field_controller_occupation(self):
        pass

    def field_controller_prefix(self):
        pass

    def field_controller_state(self):
        pass

    def field_controller_street_1(self):
        pass

    def field_controller_street_2(self):
        pass

    def field_controller_suffix(self):
        pass

    def field_controller_zip_code(self):
        pass

    def field_coordinated_expenditures(self):
        pass

    def field_c_other_political_committees_pacs(self):
        pass

    def field_c_other_political_committees(self):
        pass

    def field_coverage_from_date(self):
        pass

    def field_coverage_through_date(self):
        pass

    def field_credit_amount_this_draw(self):
        pass

    def field_creditor_city(self):
        pass

    def field_creditor_first_name(self):
        pass

    def field_creditor_last_name(self):
        pass

    def field_creditor_middle_name(self):
        pass

    def field_creditor_name(self):
        pass

    def field_creditor_organization_name(self):
        pass

    def field_creditor_prefix(self):
        pass

    def field_creditor_state(self):
        pass

    def field_creditor_street_1(self):
        pass

    def field_creditor_street_2(self):
        pass

    def field_creditor_suffix(self):
        pass

    def field_creditor_zip_code(self):
        pass

    def field_c_refund_other_political_committees(self):
        pass

    def field_c_total_loan_repayments_made(self):
        pass

    def field_c_total_loan_repayments(self):
        pass

    def field_c_total_loans(self):
        pass

    def field_custodian_city(self):
        pass

    def field_custodian_employer(self):
        pass

    def field_custodian_first_name(self):
        pass

    def field_custodian_last_name(self):
        pass

    def field_custodian_middle_name(self):
        pass

    def field_custodian_name(self):
        pass

    def field_custodian_occupation(self):
        pass

    def field_custodian_prefix(self):
        pass

    def field_custodian_state(self):
        pass

    def field_custodian_street_1(self):
        pass

    def field_custodian_street_2(self):
        pass

    def field_custodian_suffix(self):
        pass

    def field_custodian_telephone(self):
        pass

    def field_custodian_title(self):
        pass

    def field_custodian_zip_code(self):
        pass

    def field_date_day_after_general_election(self):
        pass

    def field_date_general_election(self):
        pass

    def field_date_notarized(self):
        pass

    def field_date_notary_commission_expires(self):
        pass

    def field_date_of_election(self):
        pass

    def field_date_public_distribution(self):
        pass

    def field_date_signed(self):
        pass

    def field_delaware(self):
        pass

    def field_deposit_acct_auth_date_presidential(self):
        pass

    def field_description(self):
        pass

    def field_designated_first_name(self):
        pass

    def field_designated_last_name(self):
        pass

    def field_designated_middle_name(self):
        pass

    def field_designated_prefix(self):
        pass

    def field_designated_suffix(self):
        pass

    def field_designating_committee_id_number(self):
        pass

    def field_designating_committee_name(self):
        pass

    def field_direct_candidate_support_activity(self):
        pass

    def field_direct_candidate_support(self):
        pass

    def field_direct_fundraising(self):
        pass

    def field_dist_of_columbia(self):
        pass

    def field_donation_aggregate_amount(self):
        pass

    def field_donation_amount(self):
        pass

    def field_donation_date(self):
        pass

    def field_donor_candidate_district(self):
        pass

    def field_donor_candidate_fec_id(self):
        pass

    def field_donor_candidate_first_name(self):
        pass

    def field_donor_candidate_last_name(self):
        pass

    def field_donor_candidate_middle_name(self):
        pass

    def field_donor_candidate_name(self):
        pass

    def field_donor_candidate_office(self):
        pass

    def field_donor_candidate_prefix(self):
        pass

    def field_donor_candidate_state(self):
        pass

    def field_donor_candidate_suffix(self):
        pass

    def field_donor_committee_fec_id(self):
        pass

    def field_donor_committee_name(self):
        pass

    def field_d_the_candidate(self):
        pass

    def field_d_total_contributions_refunds(self):
        pass

    def field_d_total_offsets_to_operating_expenditures(self):
        pass

    def field_effective_date(self):
        pass

    def field_ef_type(self):
        pass

    def field_election_code(self):
        pass

    def field_election_date(self):
        pass

    def field_election_district(self):
        pass

    def field_election_other_description(self):
        pass

    def field_election_state(self):
        pass

    def field_election_year(self):
        pass

    def field_end(self):
        pass

    def field_entity_type(self):
        pass

    def field_established_date(self):
        pass

    def field_estimated_value(self):
        pass

    def field_e_total_contributions_other_than_loans(self):
        pass

    def field_e_total_contributions(self):
        pass

    def field_event_activity_name(self):
        pass

    def field_event_type(self):
        pass

    def field_event_year_to_date(self):
        pass

    def field_exempt_activity(self):
        pass

    def field_exempt_legal_and_accounting_disbursements(self):
        pass

    def field_expenditure_amount(self):
        pass

    def field_expenditure_date(self):
        pass

    def field_expenditure_purpose_code(self):
        pass

    def field_expenditure_purpose_descrip(self):
        pass

    def field_expenditure_purpose_description(self):
        pass

    def field_extra_nonfederal_point(self):
        pass

    def field_F132(self):
        pass

    def field_F133(self):
        pass

    def field_F13(self):
        pass

    def field_F1M(self):
        pass

    def field_F1(self):
        pass

    def field_F1S(self):
        pass

    def field_F24(self):
        pass

    def field_F2(self):
        pass

    def field_F2S(self):
        pass

    def field_F3L(self):
        pass
#    def field_{F3L(self):
        pass

    def field_F3P31(self):
        pass

    def field_F3(self):
        pass

    def field_F3P(self):
        pass

    def field_F3PS(self):
        pass

    def field_F3S(self):
        pass

    def field_F3X(self):
        pass

    def field_F3Z(self):
        pass

    def field_F4(self):
        pass

    def field_F56(self):
        pass

    def field_F57(self):
        pass

    def field_F5(self):
        pass

    def field_F65(self):
        pass

    def field_F6(self):
        pass

    def field_F76(self):
        pass

    def field_F7(self):
        pass

    def field_F91(self):
        pass

    def field_F92(self):
        pass

    def field_F93(self):
        pass

    def field_F94(self):
        pass

    def field_F99(self):
        pass

    def field_F9(self):
        pass

    def field_f_basis_of_loan_description(self):
        pass

    def field_fec_candidate_id_number(self):
        pass

    def field_fec_committee_id_number(self):
        pass

    def field_fec_version(self):
        pass

    def field_federal_funds(self):
        pass

    def field_federal_percentage(self):
        pass

    def field_federal_percent(self):
        pass

    def field_federal_share(self):
        pass

    def field_fields(self):
        pass

    def field_fifth_candidate_contribution_date(self):
        pass

    def field_fifth_candidate_district(self):
        pass

    def field_fifth_candidate_fifth_name(self):
        pass

    def field_fifth_candidate_id_number(self):
        pass

    def field_fifth_candidate_last_name(self):
        pass

    def field_fifth_candidate_middle_name(self):
        pass

    def field_fifth_candidate_name(self):
        pass

    def field_fifth_candidate_office(self):
        pass

    def field_fifth_candidate_prefix(self):
        pass

    def field_fifth_candidate_state(self):
        pass

    def field_fifth_candidate_suffix(self):
        pass

    def field_fifty_first_contributor_date(self):
        pass

    def field_filer_code_description(self):
        pass

    def field_filer_code(self):
        pass

    def field_filer_committee_id_number(self):
        pass

    def field_first_candidate_contribution_date(self):
        pass

    def field_first_candidate_district(self):
        pass

    def field_first_candidate_first_name(self):
        pass

    def field_first_candidate_id_number(self):
        pass

    def field_first_candidate_last_name(self):
        pass

    def field_first_candidate_middle_name(self):
        pass

    def field_first_candidate_name(self):
        pass

    def field_first_candidate_office(self):
        pass

    def field_first_candidate_prefix(self):
        pass

    def field_first_candidate_state(self):
        pass

    def field_first_candidate_suffix(self):
        pass

    def field_flat_minimum_federal_percentage(self):
        pass

    def field_florida(self):
        pass

    def field_form_type(self):
        pass

    def field_fourth_candidate_contribution_date(self):
        pass

    def field_fourth_candidate_district(self):
        pass

    def field_fourth_candidate_fourth_name(self):
        pass

    def field_fourth_candidate_id_number(self):
        pass

    def field_fourth_candidate_last_name(self):
        pass

    def field_fourth_candidate_middle_name(self):
        pass

    def field_fourth_candidate_name(self):
        pass

    def field_fourth_candidate_office(self):
        pass

    def field_fourth_candidate_prefix(self):
        pass

    def field_fourth_candidate_state(self):
        pass

    def field_fourth_candidate_suffix(self):
        pass

    def field_fundraising_activity(self):
        pass

    def field_fundraising_disbursements(self):
        pass

    def field_future_income(self):
        pass

    def field_general_election(self):
        pass

    def field_general_personal_funds_declared(self):
        pass

    def field_generic_campaign_activity(self):
        pass

    def field_generic_campaign_amount(self):
        pass

    def field_generic_voter_drive_activity(self):
        pass

    def field_generic_voter_drive_ratio_applies(self):
        pass

    def field_georgia(self):
        pass

    def field_gotv_activity(self):
        pass

    def field_gotv_amount(self):
        pass

    def field_guam(self):
        pass

    def field_guaranteed_amount(self):
        pass

    def field_guarantor_city(self):
        pass

    def field_guarantor_employer(self):
        pass

    def field_guarantor_first_name(self):
        pass

    def field_guarantor_last_name(self):
        pass

    def field_guarantor_middle_name(self):
        pass

    def field_guarantor_name(self):
        pass

    def field_guarantor_occupation(self):
        pass

    def field_guarantor_prefix(self):
        pass

    def field_guarantor_state(self):
        pass

    def field_guarantor_street_1(self):
        pass

    def field_guarantor_street_2(self):
        pass

    def field_guarantor_suffix(self):
        pass

    def field_guarantor_zip_code(self):
        pass

    def field_hawaii(self):
        pass

    def field_Header(self):
        pass

    def field_house_senate_party_committees_actual_federal_candidate_support(
        self):
        pass

    def field_house_senate_party_committees_actual_nonfederal_candidate_support(
        self):
        pass

    def field_house_senate_party_committees_minimum_federal_percentage(self):
        pass

    def field_house_senate_party_committees_percentage_actual_federal(self):
        pass

    def field_house_senate_party_committees_percentage_federal_candidate_support(
        self):
        pass

    def field_house_senate_party_committees_percentage_nonfederal_candidate_support(
        self):
        pass

    def field_idaho(self):
        pass

    def field_illinois(self):
        pass

    def field_increased_limit_code(self):
        pass

    def field_increased_limit(self):
        pass

    def field_incurred_amount_this_period(self):
        pass

    def field_indiana(self):
        pass

    def field_individual_employer(self):
        pass

    def field_individual_first_name(self):
        pass

    def field_individual_last_name(self):
        pass

    def field_individual_middle_name(self):
        pass

    def field_individual_occupation(self):
        pass

    def field_individual_prefix(self):
        pass

    def field_individual_suffix(self):
        pass

    def field_ind_name_as_signed(self):
        pass

    def field_ind_name_notary(self):
        pass

    def field_iowa(self):
        pass

    def field_item_contribution_aquired_date(self):
        pass

    def field_item_description(self):
        pass

    def field_item_fair_market_value(self):
        pass

    def field_kansas(self):
        pass

    def field_kentucky(self):
        pass
#    def field_layout)(self):
        pass

    def field_leadership_pac(self):
        pass

    def field_lender_candidate_district(self):
        pass

    def field_lender_candidate_first_name(self):
        pass

    def field_lender_candidate_id_number(self):
        pass

    def field_lender_candidate_last_name(self):
        pass

    def field_lender_candidate_middle_nm(self):
        pass

    def field_lender_candidate_name(self):
        pass

    def field_lender_candidate_office(self):
        pass

    def field_lender_candidate_prefix(self):
        pass

    def field_lender_candidate_state(self):
        pass

    def field_lender_candidate_suffix(self):
        pass

    def field_lender_city(self):
        pass

    def field_lender_committee_id_number(self):
        pass

    def field_lender_first_name(self):
        pass

    def field_lender_last_name(self):
        pass

    def field_lender_middle_name(self):
        pass

    def field_lender_name(self):
        pass

    def field_lender_organization_name(self):
        pass

    def field_lender_prefix(self):
        pass

    def field_lender_state(self):
        pass

    def field_lender_street_1(self):
        pass

    def field_lender_street_2(self):
        pass

    def field_lender_suffix(self):
        pass

    def field_lender_zip_code(self):
        pass

    def field_LEVIN(self):
        pass

    def field_levin_share(self):
        pass

    def field_line(self):
        pass

    def field_loan_amount_original(self):
        pass

    def field_loan_amount(self):
        pass

    def field_loan_balance(self):
        pass

    def field_loan_due_date(self):
        pass

    def field_loan_due_date_terms(self):
        pass

    def field_loan_inccured_date_original(self):
        pass

    def field_loan_incurred_date(self):
        pass

    def field_loan_incurred_date_terms(self):
        pass

    def field_loan_interest_rate(self):
        pass

    def field_loan_interest_rate_terms(self):
        pass

    def field_loan_payment_to_date(self):
        pass

    def field_loan_restructured(self):
        pass

    def field_lobbyist_registrant_pac_2(self):
        pass

    def field_lobbyist_registrant_pac(self):
        pass

    def field_louisiana(self):
        pass

    def field_maine(self):
        pass

    def field_maryland(self):
        pass

    def field_massachusetts(self):
        pass

    def field_memo_code(self):
        pass

    def field_memo_text_description(self):
        pass

    def field_memo_text(self):
        pass

    def field_michigan(self):
        pass

    def field_minnesota(self):
        pass

    def field_mississippi(self):
        pass

    def field_missouri(self):
        pass

    def field_montana(self):
        pass

    def field_name_delim(self):
        pass

    def field_national_party_committee_percentage(self):
        pass

    def field_nebraska(self):
        pass

    def field_net_contributions(self):
        pass

    def field_net_donations(self):
        pass

    def field_net_expenditures(self):
        pass

    def field_nevada(self):
        pass

    def field_new_hampshire(self):
        pass

    def field_new_jersey(self):
        pass

    def field_new_mexico(self):
        pass
#    def field_(New(self):
        pass

    def field_new_york(self):
        pass

    def field_nonfederal_percent(self):
        pass

    def field_nonfederal_share(self):
        pass

    def field_non_presidential_non_senate_election_year(self):
        pass

    def field_north_carolina(self):
        pass

    def field_north_dakota(self):
        pass

    def field_notary_name(self):
        pass

    def field_offsets_to_operating_expenditures(self):
        pass

    def field_of(self):
        pass

    def field_ohio(self):
        pass

    def field_oklahoma(self):
        pass

    def field_operating_expenditures(self):
        pass

    def field_oregon(self):
        pass

    def field_organization_name(self):
        pass

    def field_organization_type(self):
        pass

    def field_original_amendment_date(self):
        pass

    def field_original_registration_date(self):
        pass

    def field_other_disbursements(self):
        pass

    def field_other_receipts(self):
        pass

    def field_others_liable(self):
        pass

    def field_party_code(self):
        pass

    def field_party_type(self):
        pass
#    def field_-(self):
        pass
#    def field_&(self):
        pass

    def field_payee_candidate_district(self):
        pass

    def field_payee_candidate_first_name(self):
        pass

    def field_payee_candidate_id_number(self):
        pass

    def field_payee_candidate_last_name(self):
        pass

    def field_payee_candidate_middle_name(self):
        pass

    def field_payee_candidate_name(self):
        pass

    def field_payee_candidate_office(self):
        pass

    def field_payee_candidate_prefix(self):
        pass

    def field_payee_candidate_state(self):
        pass

    def field_payee_candidate_suffix(self):
        pass

    def field_payee_city(self):
        pass

    def field_payee_cmtte_fec_id_number(self):
        pass

    def field_payee_committee_id_number(self):
        pass

    def field_payee_employer(self):
        pass

    def field_payee_first_name(self):
        pass

    def field_payee_last_name(self):
        pass

    def field_payee_middle_name(self):
        pass

    def field_payee_name(self):
        pass

    def field_payee_occupation(self):
        pass

    def field_payee_organization_name(self):
        pass

    def field_payee_prefix(self):
        pass

    def field_payee_state(self):
        pass

    def field_payee_street_1(self):
        pass

    def field_payee_street_2(self):
        pass

    def field_payee_suffix(self):
        pass

    def field_payee_zip_code(self):
        pass

    def field_payment_amount_this_period(self):
        pass

    def field_pennsylvania(self):
        pass

    def field_perfected_interest(self):
        pass

    def field_personal_funds(self):
        pass

    def field_person_completing_first_name(self):
        pass

    def field_person_completing_last_name(self):
        pass

    def field_person_completing_middle_name(self):
        pass

    def field_person_completing_name(self):
        pass

    def field_person_completing_prefix(self):
        pass

    def field_person_completing_suffix(self):
        pass

    def field_person_designated_first_name(self):
        pass

    def field_person_designated_last_name(self):
        pass

    def field_person_designated_middle_name(self):
        pass

    def field_person_designated_name(self):
        pass

    def field_person_designated_prefix(self):
        pass

    def field_person_designated_suffix(self):
        pass

    def field_person_designated_title(self):
        pass

    def field_presidential_only_election_year(self):
        pass

    def field_presidential_senate_election_year(self):
        pass

    def field_primary_election(self):
        pass

    def field_primary_personal_funds_declared(self):
        pass

    def field_public_communications_party_activity(self):
        pass

    def field_public_communications_referencing_party_ratio_applies(self):
        pass

    def field_puerto_rico(self):
        pass

    def field_purpose_of_debt_or_obligation(self):
        pass

    def field_qualified_committee(self):
        pass

    def field_qualified_non_profit(self):
        pass

    def field_qualified_nonprofit(self):
        pass

    def field_quarterly_monthly_bundled_contributions(self):
        pass

    def field_ratio_code(self):
        pass

    def field_receipt_date(self):
        pass

    def field_receipt_line_number(self):
        pass

    def field_record_id_number(self):
        pass

    def field_record_type(self):
        pass

    def field_reference_code(self):
        pass

    def field_reference_to_si_or_sl_system_code_that_identifies_the_account(
        self):
        pass

    def field_refund_amount(self):
        pass

    def field_refund_date(self):
        pass

    def field_refund_or_disposal_of_excess(self):
        pass

    def field_report_code(self):
        pass

    def field_report_id(self):
        pass

    def field_report_number(self):
        pass

    def field_REPORT(self):
        pass

    def field_report_pgi(self):
        pass

    def field_report_type(self):
        pass

    def field_requirements_met_date(self):
        pass

    def field_rhode_island(self):
        pass

    def field_runoff_election(self):
        pass

    def field_SchA(self):
        pass

    def field_SchB(self):
        pass

    def field_SchC1(self):
        pass

    def field_SchC2(self):
        pass

    def field_SchC(self):
        pass

    def field_SchD(self):
        pass

    def field_SchE(self):
        pass

    def field_SchF(self):
        pass

    def field_SchH1(self):
        pass

    def field_SchH2(self):
        pass

    def field_SchH3(self):
        pass

    def field_SchH4(self):
        pass

    def field_SchH5(self):
        pass

    def field_SchH6(self):
        pass

    def field_SchI(self):
        pass

    def field_SchL(self):
        pass

    def field_second_candidate_contribution_date(self):
        pass

    def field_second_candidate_district(self):
        pass

    def field_second_candidate_id_number(self):
        pass

    def field_second_candidate_last_name(self):
        pass

    def field_second_candidate_middle_name(self):
        pass

    def field_second_candidate_name(self):
        pass

    def field_second_candidate_office(self):
        pass

    def field_second_candidate_prefix(self):
        pass

    def field_second_candidate_second_name(self):
        pass

    def field_second_candidate_state(self):
        pass

    def field_second_candidate_suffix(self):
        pass

    def field_secured(self):
        pass

    def field_segregated_bank_account(self):
        pass

    def field_semi_annual_bundled_contributions(self):
        pass
#    def field_Semi-annual(self):
        pass

    def field_semi_annual_period_jan_june(self):
        pass

    def field_semi_annual_period_jul_dec(self):
        pass

    def field_semi_annual_period(self):
        pass

    def field_semi_annual_refunded_bundled_amt(self):
        pass

    def field_senate_only_election_year(self):
        pass

    def field_signature_first_name(self):
        pass

    def field_signature_last_name(self):
        pass

    def field_signature_middle_name(self):
        pass

    def field_signature_name(self):
        pass

    def field_signature_prefix(self):
        pass

    def field_signature_suffix(self):
        pass

    def field_signer_first_name(self):
        pass

    def field_signer_last_name(self):
        pass

    def field_signer_middle_name(self):
        pass

    def field_signer_prefix(self):
        pass

    def field_signer_suffix(self):
        pass

    def field_soft_name(self):
        pass

    def field_soft_ver(self):
        pass

    def field_south_carolina(self):
        pass

    def field_south_dakota(self):
        pass

    def field_special_election(self):
        pass

    def field_state_of_election(self):
        pass

    def field_state(self):
        pass

    def field_street_1(self):
        pass

    def field_street_2(self):
        pass

    def field_subordinate_city(self):
        pass

    def field_subordinate_committee_id_number(self):
        pass

    def field_subordinate_committee_name(self):
        pass

    def field_subordinate_state(self):
        pass

    def field_subordinate_street_1(self):
        pass

    def field_subordinate_street_2(self):
        pass

    def field_subordinate_zip_code(self):
        pass

    def field_subtotal_federal(self):
        pass

    def field_subtotal(self):
        pass

    def field_support_oppose_code(self):
        pass

    def field_tennessee(self):
        pass

    def field_texas(self):
        pass

    def field_text_code(self):
        pass

    def field_TEXT(self):
        pass

    def field_third_candidate_contribution_date(self):
        pass

    def field_third_candidate_district(self):
        pass

    def field_third_candidate_id_number(self):
        pass

    def field_third_candidate_last_name(self):
        pass

    def field_third_candidate_middle_name(self):
        pass

    def field_third_candidate_name(self):
        pass

    def field_third_candidate_office(self):
        pass

    def field_third_candidate_prefix(self):
        pass

    def field_third_candidate_state(self):
        pass

    def field_third_candidate_suffix(self):
        pass

    def field_third_candidate_third_name(self):
        pass

    def field_this(self):
        pass

    def field_to(self):
        pass

    def field_total_amount(self):
        pass

    def field_total_amount_transferred(self):
        pass

    def field_total_balance(self):
        pass

    def field_total_contribution(self):
        pass

    def field_total_costs(self):
        pass

    def field_total_disbursements(self):
        pass

    def field_total_donations_accepted(self):
        pass

    def field_total_donations(self):
        pass

    def field_total_donations_refunded(self):
        pass

    def field_total_independent_expenditure(self):
        pass

    def field_total_points(self):
        pass

    def field_total_receipts(self):
        pass

    def field_totals(self):
        pass

    def field_TOTALS(self):
        pass

    def field_transaction_code(self):
        pass

    def field_transaction_description(self):
        pass

    def field_transaction_id_number(self):
        pass

    def field_transaction_id(self):
        pass

    def field_transaction_type(self):
        pass

    def field_transferred_amount(self):
        pass

    def field_transfers_from_aff_other_party_committees(self):
        pass

    def field_transfers_from_other_auth_committees(self):
        pass

    def field_transfers_to_other_auth_committees(self):
        pass

    def field_transfers_to_other_authorized_committees(self):
        pass

    def field_treasurer_city(self):
        pass

    def field_treasurer_first_name(self):
        pass

    def field_treasurer_last_name(self):
        pass

    def field_treasurer_middle_name(self):
        pass

    def field_treasurer_name(self):
        pass

    def field_treasurer_prefix(self):
        pass

    def field_treasurer_state(self):
        pass

    def field_treasurer_street_1(self):
        pass

    def field_treasurer_street_2(self):
        pass

    def field_treasurer_suffix(self):
        pass

    def field_treasurer_telephone(self):
        pass

    def field_treasurer_title(self):
        pass

    def field_treasurer_zip_code(self):
        pass

    def field_utah(self):
        pass

    def field_vermont(self):
        pass

    def field_virginia(self):
        pass

    def field_virgin_islands(self):
        pass

    def field_voter_id_activity(self):
        pass

    def field_voter_id_amount(self):
        pass

    def field_voter_registration_activity(self):
        pass

    def field_voter_registration_amount(self):
        pass

    def field_washington(self):
        pass

    def field_west_virginia(self):
        pass

    def field_wisconsin(self):
        pass

    def field_wyoming(self):
        pass
#    def field_YEAR-TO-DATE(self):
        pass

    def field_YTD(self):
        pass

    def field_zip_code(self):
        pass


    def startHeader(self):
        self.state = STATE_HEADER
        dbg ( "start HEADER")

    def header_line(self, line):
        parts = line.split('=')
        if (len(parts) > 1):
            self.current.attributes[parts[0]] = parts[1]


    def endHeader(self):
        dbg ( "END HEADER" )
        self.state = STATE_BODY

    def HDR(self, l, quote=""):
        dbg ( "HEADER LINE %s %s " % ( l, l.split(",")))
        parts = l.split(",")
        header = parts[0]
        fec = parts[1]
        version = parts[2]

        self.header=Header(header,fec,version)
        self.state = STATE_BODY

    def delimiter(self, filing_version):
        if (filing_version.to_f < 6):
            return  ","
        return "\034"

    def filing_url(self):
        return "http://query.nictusa.com/dcdev/posted/#{filing_id}.fec"

    def parse_file_data_line(self, l):
    #        if re.match(r'\034',l):
        if l.find("\034") > 0:
            dbg ( "found 034 in %s" % l)
            #if first.index("\034").nil?

        if re.match(r'\/\* Header', l):
            self.startHeader()
            return

        if re.match(r'\/\* End Header', l):
            self.endHeader()
            return
        if re.match(r'HDR', l):
            self.HDR(l)
            return
        if re.match(r'\'HDR\'', l):
            self.HDR(l, quote='\'')
            return
        if re.match(r'\"HDR\"', l):
            self.HDR(l, quote='\"')
            return

        if self.state == STATE_HEADER:
            dbg ( "in header %s" %  l)
            self.header_line(l)
            return

        if self.state == STATE_BODY:
            dbg ( "in body %s" % l)
            self.body_line(l)
            # call into the base class fech_rendered_maps

    def body_line(self, line):
        u"""
        the body function
        """
        version = None
        if version_field_name in self.current.attributes:
                version = self.current.attributes[version_field_name]
                #         print ("check version: ",
                #                "version:",version,
                #                "attr:",self.current.attributes
                #            )
        else:
            print("no version: ",
                  "version:", version,
                  "attr:", self.current.attributes
                  )

        body = line.split(",")
        for field_regex in self.rendered_maps.keys():
            btype = body[0]

            g = re.findall("(" + field_regex + ")", btype, re.IGNORECASE)
            if (g is not None):
                if (len(g) > 0):
                    print("check: ",
                          "regex:", field_regex,
                          "group", g,
                          "btype:", btype,
                          "version:", version,
                          "body:", body)

                    if (version is not None):
                        for version_regex in self.rendered_maps[field_regex].keys():
                            rest_of_data = self.rendered_maps[
                                field_regex][version_regex]
                            #TODO: use rest_of_data
                            g = re.findall(
                                "(" + version_regex + ")",
                                version,
                                re.IGNORECASE)
                            if (g is not None):
                                if (len(g) > 0):
                                    print(
                                        "check2: ", field_regex, g, btype, version, body, self.rendered_maps[field_regex][version_regex])

        #print l
        #                v=l.split("")
        #                self.generate(v,classname)
        #                return

    def parse_file_data(self, d):
        self.current = FileObject()
        for l in d.split("\n")[0:20]:
            self.parse_file_data_line(l)
        dbg ( "COLLECTED %s" % self.current.attributes)
        self.current = None

    def generate(self, v, name):
        c = 0

        for f in v:
            f = f.strip(" ").rstrip(" ")
            f = f.strip("\"").rstrip("\"")
            dbg ( "    %s=%d" % (f, c))
            c = c + 1
