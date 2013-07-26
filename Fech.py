#porting of fetch to python
#code borrowed from https://github.com/NYTimes/Fech
#wich is under the apache license https://github.com/NYTimes/Fech/blob/master/LICENSE
import re 

#state enum
STATE_UNKNOWN=0
STATE_HEADER=1
STATE_BODY=2

class Parser :

  
  # Converts symbols and strings to Regexp objects for use in regex-keyed maps.
  # Assumes that symbols should be matched literally, strings unanchored.
  # @param [String,Symbol,Regexp] label the object to convert to a Regexp
    def regexify(self, label):
        if label in self.ROW_TYPES_REGEX :
            return ROW_TYPES[label]
        else:
            return r("^#{label.to_s}$")

    def RowTypes_hdr() : 
        pass
    def RowTypes_f1():
        pass
    def RowTypes_f13():
        pass
    def RowTypes_f132():
        pass
    def  RowTypes_f133():
        pass
    def RowTypes_f1m():
        pass
    def RowTypes_f2():
        pass
    def RowTypes_f24():
        pass
    def RowTypes_f3():
        pass
    def RowTypes_f3l():
        pass
    def RowTypes_f3p():
        pass
    def RowTypes_f3s():
        pass
    def RowTypes_f3p31():
        pass
    def RowTypes_f3ps():
        pass
    def RowTypes_f3x():
        pass
    def RowTypes_f4():
        pass
    def RowTypes_f5():
        pass
    def RowTypes_f56():
        pass
    def RowTypes_f57():
        pass
    def RowTypes_f6():
        pass
    def RowTypes_f65():
        pass
    def RowTypes_f7():
        pass
    def RowTypes_f76():
        pass
    def RowTypes_f9():
        pass
    def RowTypes_f91():
        pass
    def RowTypes_f92():
        pass
    def RowTypes_f93():
        pass
    def RowTypes_f94():
        pass
    def RowTypes_f99():
        pass
    def RowTypes_h1():
        pass
    def RowTypes_h2():
        pass
    def RowTypes_h3():
        pass
    def RowTypes_h4():
        pass
    def RowTypes_h5():
        pass
    def RowTypes_h6():
        pass
    def RowTypes_sa():
        pass
    def RowTypes_sb():
        pass
    def RowTypes_sc():
        pass
    def RowTypes_sc1():
        pass
    def RowTypes_sc2():
        pass
    def RowTypes_sd():
        pass
    def RowTypes_se():
        pass
    def RowTypes_sf():
        pass
    def RowTypes_sl():
        pass
    def RowTypes_text():
        pass
 
     #add
    def field_11_a_iii_individuals_total():pass
    def field_11_a_ii_individuals_unitemized():pass
    def field_11_a_i_individuals_itemized():pass
    def field_11_b_political_party_committees():pass
    def field_11_c_all_other_political_committees_pacs():pass
    def field_11_d_the_candidate():pass
    def field_11_e_total_contributions():pass
    def field_12_transfers_from_other_auth_committees():pass
    def field_13_a_loans_made_or_guarn_by_the_candidate():pass
    def field_13_b_all_other_loans():pass
    def field_13_c_total_loans():pass
    def field_14_net_contributions():pass
    def field_14_offsets_to_operating_expenditures():pass
    def field_15_net_expenditures():pass
    def field_15_other_receipts():pass
    def field_16_federal_funds():pass
    def field_16_total_receipts():pass
    def field_17_a_iii_individual_contribution_total():pass
    def field_17_a_ii_individuals_unitemized():pass
    def field_17_a_i_individuals_itemized():pass
    def field_17_a_individuals():pass
    def field_17_b_political_party_committees():pass
    def field_17_c_other_political_committees_pacs():pass
    def field_17_d_the_candidate():pass
    def field_17_e_total_contributions_other_than_loans():pass
    def field_17_operating_expenditures():pass
    def field_18_transfers_from_aff_other_party_committees():pass
    def field_18_transfers_to_other_auth_committees():pass
    def field_19_a_loan_repayment_by_candidate():pass
    def field_19_a_received_from_or_guaranteed_by_candidate():pass
    def field_19_b_loan_repayments_all_other_loans():pass
    def field_19_b_other_loans():pass
    def field_19_c_total_loan_repayments():pass
    def field_19_c_total_loans():pass
    def field_20_a_operating():pass
    def field_20_a_refund_individuals_other_than_pol_cmtes():pass
    def field_20_b_fundraising():pass
    def field_20_b_refund_political_party_committees():pass
    def field_20_c_legal_and_accounting():pass
    def field_20_c_refund_other_political_committees():pass
    def field_20_d_total_contributions_refunds():pass
    def field_20_d_total_offsets_to_operating_expenditures():pass
    def field_21_other_disbursements():pass
    def field_21_other_receipts():pass
    def field_22_total_disbursements():pass
    def field_22_total_receipts():pass
    def field_23_operating_expenditures():pass
    def field_24_transfers_to_other_authorized_committees():pass
    def field_25_fundraising_disbursements():pass
    def field_26_exempt_legal_and_accounting_disbursements():pass
    def field_27_a_made_or_guaranteed_by_the_candidate():pass
    def field_27_b_other_repayments():pass
    def field_27_c_total_loan_repayments_made():pass
    def field_28_a_individuals():pass
    def field_28_b_political_party_committees():pass
    def field_28_c_other_political_committees():pass
    def field_28_d_total_contributions_refunds():pass
    def field_29_other_disbursements():pass
    def field_30():pass
    def field_30_total_disbursements():pass
    def field_6a_total_contributions_no_loans():pass
    def field_6b_total_contribution_refunds():pass
    def field_6c_net_contributions():pass
    def field_7a_total_operating_expenditures():pass
    def field_7b_total_offsets_to_operating_expenditures():pass
    def field_7c_net_operating_expenditures():pass
    def field_account_identifier():pass
    def field_account_location_name():pass
    def field_account_name():pass
    def field_activity_event_name():pass
    def field_activity_general():pass
    def field_ACTIVITY():pass
    def field_activity_primary():pass
    def field_actual_direct_candidate_support_federal():pass
    def field_actual_direct_candidate_support_federal_percent():pass
    def field_actual_direct_candidate_support_nonfederal():pass
    def field_added():pass
    def field_administrative_ratio_applies():pass
    def field_administrative_voter_drive_activity():pass
    def field_affiliated_candidate_id_number():pass
    def field_affiliated_city():pass
    def field_affiliated_committee_id_number():pass
    def field_affiliated_committee_name():pass
    def field_affiliated_date_f1_filed():pass
    def field_affiliated_first_name():pass
    def field_affiliated_last_name():pass
    def field_affiliated_middle_name():pass
    def field_affiliated_prefix():pass
    def field_affiliated_relationship_code():pass
    def field_affiliated_state():pass
    def field_affiliated_street_1():pass
    def field_affiliated_street_2():pass
    def field_affiliated_suffix():pass
    def field_affiliated_zip_code():pass
    def field_agent_city():pass
    def field_agent_first_name():pass
    def field_agent_last_name():pass
    def field_agent_middle_name():pass
    def field_agent_name():pass
    def field_agent_prefix():pass
    def field_agent_state():pass
    def field_agent_street_1():pass
    def field_agent_street_2():pass
    def field_agent_suffix():pass
    def field_agent_telephone():pass
    def field_agent_title():pass
    def field_agent_zip_code():pass
    def field_aggregate_general_elec_expended():pass
    def field_a_iii_individual_contribution_total():pass
    def field_a_iii_individuals_total():pass
    def field_a_ii_individuals_unitemized():pass
    def field_a_i_individuals_itemized():pass
    def field_a_individuals():pass
    def field_alabama():pass
    def field_alaska():pass
    def field_a_loan_repayment_by_candidate():pass
    def field_a_loans_made_or_guarn_by_the_candidate():pass
    def field_a_made_or_guaranteed_by_the_candidate():pass
    def field_amended_cd():pass
    def field_amended_code():pass
    def field_amendment_date():pass
    def field_a_operating():pass
    def field_A():pass
    def field_a_received_from_or_guaranteed_by_candidate():pass
    def field_a_refund_individuals_other_than_pol_cmtes():pass
    def field_arizona():pass
    def field_arkansas():pass
    def field_a_total_contributions_no_loans():pass
    def field_a_total_operating_expenditures():pass
    def field_at():pass
    def field_authorized_committee_city():pass
    def field_authorized_committee_id_number():pass
    def field_authorized_committee_name():pass
    def field_authorized_committee_state():pass
    def field_authorized_committee_street_1():pass
    def field_authorized_committee_street_2():pass
    def field_authorized_committee_zip_code():pass
    def field_authorized_first_name():pass
    def field_authorized_last_name():pass
    def field_authorized_middle_name():pass
    def field_authorized_name():pass
    def field_authorized_prefix():pass
    def field_authorized_suffix():pass
    def field_authorized_title():pass
    def field_back_reference_sched_form_name():pass
    def field_back_reference_sched_name():pass
    def field_back_reference_tran_id_number():pass
    def field_balance_at_close_this_period():pass
    def field_ballot_governor():pass
    def field_b_all_other_loans():pass
    def field_ballot_house():pass
    def field_ballot_local_candidates():pass
    def field_ballot_other_statewide():pass
    def field_ballot_presidential():pass
    def field_ballot_senate():pass
    def field_ballot_state_representative():pass
    def field_ballot_state_senate():pass
    def field_bank2_city():pass
    def field_bank2_name():pass
    def field_bank2_state():pass
    def field_bank2_street_1():pass
    def field_bank2_street_2():pass
    def field_bank2_zip_code():pass
    def field_bank_city():pass
    def field_bank_name():pass
    def field_bank_state():pass
    def field_bank_street_1():pass
    def field_bank_street_2():pass
    def field_bank_zip_code():pass
    def field_beginning_balance_this_period():pass
    def field_beneficiary_candidate_district():pass
    def field_beneficiary_candidate_fec_id():pass
    def field_beneficiary_candidate_first_name():pass
    def field_beneficiary_candidate_last_name():pass
    def field_beneficiary_candidate_middle_name():pass
    def field_beneficiary_candidate_name():pass
    def field_beneficiary_candidate_office():pass
    def field_beneficiary_candidate_prefix():pass
    def field_beneficiary_candidate_state():pass
    def field_beneficiary_candidate_suffix():pass
    def field_beneficiary_committee_fec_id():pass
    def field_beneficiary_committee_name():pass
    def field_b_fundraising():pass
    def field_b_loan_repayments_all_other_loans():pass
    def field_b_other_loans():pass
    def field_b_other_repayments():pass
    def field_B():pass
    def field_b_political_party_committees():pass
    def field_b_refund_political_party_committees():pass
    def field_b_total_contribution_refunds():pass
    def field_b_total_offsets_to_operating_expenditures():pass
#    def field_Bundled}"():pass
    def field_calendar_y_t_d_per_election_office():pass
    def field_california():pass
    def field_c_all_other_political_committees_pacs():pass
    def field_candidate_city():pass
    def field_candidate_district():pass
    def field_candidate_first_name():pass
    def field_candidate_id_number():pass
    def field_candidate_id():pass
    def field_candidate_last_name():pass
    def field_candidate_middle_name():pass
    def field_candidate_name():pass
    def field_candidate_office():pass
    def field_candidate_party_code():pass
    def field_candidate_prefix():pass
    def field_candidate_signature_first_name():pass
    def field_candidate_signature_last_name():pass
    def field_candidate_signature_middle_name():pass
    def field_candidate_signature_name():pass
    def field_candidate_signature_prefix():pass
    def field_candidate_signature_suffix():pass
    def field_candidate_state():pass
    def field_candidate_street_1():pass
    def field_candidate_street_2():pass
    def field_candidate_suffix():pass
    def field_candidate_zip_code():pass
    def field_canonical():pass
    def field_category_code():pass
    def field_change_of_address():pass
    def field_change_of_committee_email():pass
    def field_change_of_committee_name():pass
    def field_change_of_committee_url():pass
    def field_city():pass
    def field_c_legal_and_accounting():pass
    def field_c_net_contributions():pass
    def field_c_net_operating_expenditures():pass
    def field_col_a_alabama():pass
    def field_col_a_alaska():pass
    def field_col_a_arizona():pass
    def field_col_a_arkansas():pass
    def field_col_a_california():pass
    def field_col_a_candidate_contributions():pass
    def field_col_a_candidate_loan_repayments():pass
    def field_col_a_candidate_loans():pass
    def field_col_a_cash_beginning_reporting_period():pass
    def field_col_a_cash_on_hand_beginning_period():pass
    def field_col_a_cash_on_hand_beginning_reporting_period():pass
    def field_col_a_cash_on_hand_close_of_period():pass
    def field_col_a_cash_on_hand_close():pass
    def field_col_a_colorado():pass
    def field_col_a_connecticut():pass
    def field_col_a_contributions_itemized():pass
    def field_col_a_contributions_subtotal():pass
    def field_col_a_contributions_to_candidates():pass
    def field_col_a_contributions_unitemized():pass
    def field_col_a_convention_expenditures():pass
    def field_col_a_convention_expenses_itemized():pass
    def field_col_a_convention_expenses_subtotal():pass
    def field_col_a_convention_expenses_unitemized():pass
    def field_col_a_convention_refunds_itemized():pass
    def field_col_a_convention_refunds():pass
    def field_col_a_convention_refunds_subtotal():pass
    def field_col_a_convention_refunds_unitemized():pass
    def field_col_a_coordinated_expenditures_by_party_committees():pass
    def field_col_a_debts_by():pass
    def field_col_a_debts_to():pass
    def field_col_a_delaware():pass
    def field_col_a_disbursements_subtotal():pass
    def field_col_a_dist_of_columbia():pass
    def field_col_a_exempt_legal_accounting_disbursement():pass
    def field_col_a_expenditures_subject_to_limits():pass
    def field_col_a_federal_election_activity_all_federal():pass
    def field_col_a_federal_election_activity_federal_share():pass
    def field_col_a_federal_election_activity_levin_share():pass
    def field_col_a_federal_election_activity_total():pass
    def field_col_a_federal_funds():pass
    def field_col_a_florida():pass
    def field_col_a_fundraising_disbursements():pass
    def field_col_a_fundraising():pass
    def field_col_a_generic_campaign_disbursements():pass
    def field_col_a_georgia():pass
    def field_col_a_gotv_disbursements():pass
    def field_col_a_guam():pass
    def field_col_a_hawaii():pass
    def field_col_a_idaho():pass
    def field_col_a_illinois():pass
    def field_col_a_independent_expenditures():pass
    def field_col_a_indiana():pass
    def field_col_a_individual_contributions_itemized():pass
    def field_col_a_individual_contributions_itemized(): pass
    def field_col_a_individual_contributions_unitemized():pass
    def field_col_a_individual_contribution_total():pass
    def field_col_a_individuals_itemized():pass
    def field_col_a_individuals():pass
    def field_col_a_individuals_unitemized():pass
    def field_col_a_iowa():pass
    def field_col_a_itemized_receipts_persons():pass
    def field_col_a_items_on_hand_to_be_liquidated():pass
    def field_col_a_kansas():pass
    def field_col_a_kentucky():pass
    def field_col_a_legal_and_accounting():pass
    def field_col_a_levin_funds():pass
    def field_col_a_loan_disbursements_subtotal():pass
    def field_col_a_loan_receipts_subtotal():pass
    def field_col_a_loan_repayments_made():pass
    def field_col_a_loan_repayments_received():pass
    def field_col_a_loans_made():pass
    def field_col_a_loans_received():pass
    def field_col_a_louisiana():pass
    def field_col_a_made_or_guaranteed_by_candidate():pass
    def field_col_a_maine():pass
    def field_col_a_maryland():pass
    def field_col_a_massachusetts():pass
    def field_col_a_michigan():pass
    def field_col_a_minnesota():pass
    def field_col_a_mississippi():pass
    def field_col_a_missouri():pass
    def field_col_a_montana():pass
    def field_col_a_nebraska():pass
    def field_col_a_net_contributions():pass
    def field_col_a_net_operating_expenditures():pass
    def field_col_a_nevada():pass
    def field_col_a_new_hampshire():pass
    def field_col_a_new_jersey():pass
    def field_col_a_new_mexico():pass
    def field_col_a_new_york():pass
    def field_col_a_north_carolina():pass
    def field_col_a_north_dakota():pass
    def field_col_a_offsets_to_expenditures():pass
    def field_col_a_offset_to_operating_expenditures():pass
    def field_col_a_ohio():pass
    def field_col_a_oklahoma():pass
    def field_col_a_operating_expenditures():pass
    def field_col_a_operating():pass
    def field_col_a_oregon():pass
    def field_col_a_other_disbursements_itemized():pass
    def field_col_a_other_disbursements():pass
    def field_col_a_other_disbursements_subtotal():pass
    def field_col_a_other_disbursements_unitemized():pass
    def field_col_a_other_federal_operating_expenditures():pass
    def field_col_a_other_federal_receipts():pass
    def field_col_a_other_income_itemized():pass
    def field_col_a_other_income_subtotal():pass
    def field_col_a_other_income_unitemized():pass
    def field_col_a_other_loan_repayments():pass
    def field_col_a_other_loans():pass
    def field_col_a_other_political_committees_pacs():pass
    def field_col_a_other_political_committees():pass
    def field_col_a_other_receipts():pass
    def field_col_a_other_refunds_itemized():pass
    def field_col_a_other_refunds_subtotal():pass
    def field_col_a_other_refunds_unitemized():pass
    def field_col_a_other_repayments():pass
    def field_col_a_pac_contributions():pass
    def field_col_a_pennsylvania():pass
    def field_text():pass
    def field_nonfederal_percentage():pass
    def field_rec_type():pass
    def field_col_b_gross_receipts_minus_personal_funds_general():pass 
    def field_col_a_political_party_committees():pass
    def field_col_a_political_party_committees_receipts():pass
    def field_col_a_political_party_committees_refunds():pass
    def field_col_a_political_party_contributions():pass
    def field_col_a_political_party_contributions():pass
    def field_col_a_pac_contributions():pass
    def field_col_a_prior_expenditures_subject_to_limits():pass
    def field_col_a_puerto_rico():pass
    def field_col_a_receipts_period():pass
    def field_col_a_received_from_or_guaranteed_by_cand():pass
    def field_col_a_refunds_to_individuals():pass
    def field_col_a_refunds_to_other_committees():pass
    def field_col_a_refunds_to_party_committees():pass
    def field_col_a_rhode_island():pass
    def field_col_a_shared_operating_expenditures_federal():pass
    def field_col_a_shared_operating_expenditures_nonfederal():pass
    def field_col_a_south_carolina():pass
    def field_col_a_south_dakota():pass
    def field_col_a_subtotal():pass
    def field_col_a_subtotal_period():pass
    def field_col_a_tennessee():pass
    def field_col_a_texas():pass
    def field_col_a_the_candidate():pass
    def field_col_a_total_contributions_no_loans():pass
    def field_col_a_total_contributions():pass
    def field_col_a_total_contributions_refunds():pass
    def field_col_a_total_disbursements():pass
    def field_col_a_total_expenditures_subject_to_limits():pass
    def field_col_a_total_federal_disbursements():pass
    def field_col_a_total_federal_operating_expenditures():pass
    def field_col_a_total_federal_receipts():pass
    def field_col_a_total_individual_contributions():pass
    def field_col_a_total_loan_repayments_made():pass
    def field_col_a_total_loan_repayments():pass
    def field_col_a_total_loan_repayments_received():pass
    def field_col_a_total_loans():pass
    def field_col_a_total_nonfederal_transfers():pass
    def field_col_a_total_offsets_to_expenditures():pass
    def field_col_a_total_offsets_to_operating_expenditures():pass
    def field_col_a_total_offset_to_operating_expenditures():pass
    def field_col_a_total_operating_expenditures():pass
    def field_col_a_total_receipts():pass
    def field_col_a_total_receipts_period():pass
    def field_col_a_total_receipts_persons():pass
    def field_col_a_total_refunds():pass
    def field_col_a_totals():pass
    def field_col_a_transfers_from_aff_other_party_cmttees():pass
    def field_col_a_transfers_from_authorized():pass
    def field_col_a_transfers_from_nonfederal_h3():pass
    def field_col_a_transfers_to_affiliated():pass
    def field_col_a_transfers_to_authorized():pass
    def field_col_a_transfers_to_other_authorized_committees():pass
    def field_col_a_unitemized_receipts_persons():pass
    def field_col_a_utah():pass
    def field_col_a_vermont():pass
    def field_col_a_virginia():pass
    def field_col_a_virgin_islands():pass
    def field_col_a_voter_id_disbursements():pass
    def field_col_a_voter_registration_disbursements():pass
    def field_col_a_washington():pass
    def field_col_a_west_virginia():pass
    def field_col_a_wisconsin():pass
    def field_col_a_wyoming():pass
    def field_col_b_aggregate_personal_funds_general():pass
    def field_col_b_aggregate_personal_funds_primary():pass
    def field_col_b_alabama():pass
    def field_col_b_alaska():pass
    def field_col_b_arizona():pass
    def field_col_b_arkansas():pass
    def field_col_b_beginning_year():pass
    def field_col_b_california():pass
    def field_col_b_candidate_contributions():pass
    def field_col_b_candidate_loan_repayments():pass
    def field_col_b_candidate_loans():pass
    def field_col_b_cash_on_hand_beginning_period():pass
    def field_col_b_cash_on_hand_beginning_year():pass
    def field_col_b_cash_on_hand_close_of_period():pass
    def field_col_b_cash_on_hand_jan_1():pass
    def field_col_b_colorado():pass
    def field_col_b_connecticut():pass
    def field_col_b_contributions_subtotal():pass
    def field_col_b_contributions_to_candidates():pass
    def field_col_b_convention_expenditures():pass
    def field_col_b_convention_expenses_subtotal():pass
    def field_col_b_convention_refunds():pass
    def field_col_b_convention_refunds_subtotal():pass
    def field_col_b_coordinated_expenditures_by_party_committees():pass
    def field_col_b_delaware():pass
    def field_col_b_disbursements_period():pass
    def field_col_b_disbursements_subtotal():pass
    def field_col_b_dist_of_columbia():pass
    def field_col_b_exempt_legal_accounting_disbursement():pass
    def field_col_b_expenditures_subject_to_limits():pass
    def field_col_b_federal_election_activity_all_federal():pass
    def field_col_b_federal_election_activity_federal_share():pass
    def field_col_b_federal_election_activity_levin_share():pass
    def field_col_b_federal_election_activity_total():pass
    def field_col_b_federal_funds():pass
    def field_col_b_florida():pass
    def field_col_b_fundraising_disbursements():pass
    def field_col_b_fundraising():pass
    def field_col_b_generic_campaign_disbursements():pass
    def field_col_b_georgia():pass
    def field_col_b_gotv_disbursements():pass
    def field_col_b_gross_receipts_authorized_general():pass
    def field_col_b_gross_receipts_authorized_primary():pass
    def field_col_b_gross_receipts_minus_personal_funds_primary():pass
    def field_col_b_guam():pass
    def field_col_b_hawaii():pass
    def field_col_b_idaho():pass
    def field_col_b_illinois():pass
    def field_col_b_independent_expenditures():pass
    def field_col_b_indiana():pass
    def field_col_b_individual_contributions_itemized():pass
    def field_col_b_individual_contributions_unitemized():pass
    def field_col_b_individual_contribution_total():pass
    def field_col_b_individuals_itemized():pass
    def field_col_b_individuals():pass
    def field_col_b_individuals_unitemized():pass
    def field_col_b_iowa():pass
    def field_col_b_itemized_receipts_persons():pass
    def field_col_b_kansas():pass
    def field_col_b_kentucky():pass
    def field_col_b_legal_and_accounting():pass
    def field_col_b_levin_funds():pass
    def field_col_b_loan_disbursements_subtotal():pass
    def field_col_b_loan_receipts_subtotal():pass
    def field_col_b_loans_made():pass
    def field_col_b_louisiana():pass
    def field_col_b_made_or_guaranteed_by_the_candidate():pass
    def field_col_b_maine():pass
    def field_col_b_maryland():pass
    def field_col_b_massachusetts():pass
    def field_col_b_michigan():pass
    def field_col_b_minnesota():pass
    def field_col_b_mississippi():pass
    def field_col_b_missouri():pass
    def field_col_b_montana():pass
    def field_col_b_nebraska():pass
    def field_col_b_net_contributions():pass
    def field_col_b_net_operating_expenditures():pass
    def field_col_b_nevada():pass
    def field_col_b_new_hampshire():pass
    def field_col_b_new_jersey():pass
    def field_col_b_new_mexico():pass
    def field_col_b_new_york():pass
    def field_col_b_north_carolina():pass
    def field_col_b_north_dakota():pass
    def field_col_b_offsets_to_expenditures():pass
    def field_col_b_offset_to_operating_expenditures():pass
    def field_col_b_ohio():pass
    def field_col_b_oklahoma():pass
    def field_col_b_operating_expenditures():pass
    def field_col_b_operating():pass
    def field_col_b_oregon():pass
    def field_col_b_other_disbursements():pass
    def field_col_b_other_disbursements_subtotal():pass
    def field_col_b_other_federal_operating_expenditures():pass
    def field_col_b_other_federal_receipts():pass
    def field_col_b_other_income_subtotal():pass
    def field_col_b_other_loan_repayments():pass
    def field_col_b_other_loans():pass
    def field_col_b_other_political_committees_pacs():pass
    def field_col_b_other_political_committees():pass
    def field_col_b_other_receipts():pass
    def field_col_b_other_refunds_subtotal():pass
    def field_col_b_other_repayments():pass
    def field_col_b_pac_contributions():pass
    def field_col_b_pennsylvania():pass
    def field_col_b_political_party_committees():pass
    def field_col_b_political_party_committees_receipts():pass
    def field_col_b_political_party_committees_refunds():pass
    def field_col_b_political_party_contributions():pass
    def field_col_b_prior_expendiutres_subject_to_limits():pass
    def field_col_b_puerto_rico():pass
    def field_col_b_receipts_period():pass
    def field_col_b_received_from_or_guaranteed_by_cand():pass
    def field_col_b_refunds_to_individuals():pass
    def field_col_b_refunds_to_other_committees():pass
    def field_col_b_refunds_to_party_committees():pass
    def field_col_b_rhode_island():pass
    def field_col_b_shared_operating_expenditures_federal():pass
    def field_col_b_shared_operating_expenditures_nonfederal():pass
    def field_col_b_south_carolina():pass
    def field_col_b_south_dakota():pass
    def field_col_b_subtotal():pass
    def field_col_b_subtotal_period():pass
    def field_col_b_tennessee():pass
    def field_col_b_texas():pass
    def field_col_b_the_candidate():pass
    def field_col_b_total_contributions_no_loans():pass
    def field_col_b_total_contributions_other_than_loans():pass
    def field_col_b_total_contributions():pass
    def field_col_b_total_contributions_refunds():pass
    def field_col_b_total_disbursements():pass
    def field_col_b_total_expenditures_subject_to_limits():pass
    def field_col_b_total_federal_disbursements():pass
    def field_col_b_total_federal_operating_expenditures():pass
    def field_col_b_total_federal_receipts():pass
    def field_col_b_total_individual_contributions():pass
    def field_col_b_total_loan_repayments_made():pass
    def field_col_b_total_loan_repayments():pass
    def field_col_b_total_loan_repayments_received():pass
    def field_col_b_total_loans():pass
    def field_col_b_total_nonfederal_transfers():pass
    def field_col_b_total_offsets_to_expenditures():pass
    def field_col_b_total_offsets_to_operating_expenditures():pass
    def field_col_b_total_offset_to_operating_expenditures():pass
    def field_col_b_total_operating_expenditures():pass
    def field_col_b_total_receipts():pass
    def field_col_b_total_receipts_persons():pass
    def field_col_b_total_refunds():pass
    def field_col_b_totals():pass
    def field_col_b_transfers_from_affiliated():pass
    def field_col_b_transfers_from_aff_other_party_cmttees():pass
    def field_col_b_transfers_from_authorized():pass
    def field_col_b_transfers_from_nonfederal_h3():pass
    def field_col_b_transfers_to_affiliated():pass
    def field_col_b_transfers_to_authorized():pass
    def field_col_b_transfers_to_other_authorized_committees():pass
    def field_col_b_unitemized_receipts_persons():pass
    def field_col_b_utah():pass
    def field_col_b_vermont():pass
    def field_col_b_virginia():pass
    def field_col_b_virgin_islands():pass
    def field_col_b_voter_id_disbursements():pass
    def field_col_b_voter_registration_disbursements():pass
    def field_col_b_washington():pass
    def field_col_b_west_virginia():pass
    def field_col_b_wisconsin():pass
    def field_col_b_wyoming():pass
    def field_col_b_year():pass
    def field_collateral():pass
    def field_collateral_value_amount():pass
    def field_colorado():pass
    def field_COLUMN():pass
    def field_comment():pass
    def field_committee_city():pass
    def field_committee_email():pass
    def field_committee_fax_number():pass
    def field_committee_id_number():pass
    def field_committee_name():pass
    def field_committee_state():pass
    def field_committee_street_1():pass
    def field_committee_street_2():pass
    def field_committee_type_description():pass
    def field_committee_type():pass
    def field_committee_url():pass
    def field_committee_zip_code():pass
    def field_communication_class():pass
    def field_communication_cost():pass
    def field_communication_date():pass
    def field_communication_title():pass
    def field_communication_type_description():pass
    def field_communication_type():pass
    def field_completing_first_name():pass
    def field_completing_last_name():pass
    def field_completing_middle_name():pass
    def field_completing_prefix():pass
    def field_completing_suffix():pass
    def field_conduit_city():pass
    def field_conduit_committee_id():pass
    def field_conduit_name():pass
    def field_conduit_state():pass
    def field_conduit_street_1():pass
    def field_conduit_street1():pass
    def field_conduit_street_2():pass
    def field_conduit_street2():pass
    def field_conduit_zip_code():pass
    def field_connecticut():pass
    def field_contribution_aggregate():pass
    def field_contribution_amount():pass
    def field_contribution_date():pass
    def field_contribution_purpose_code():pass
    def field_contribution_purpose_descrip():pass
    def field_contributor_city():pass
    def field_contributor_employer():pass
    def field_contributor_fec_id():pass
    def field_contributor_first_name():pass
    def field_contributor_last_name():pass
    def field_contributor_middle_name():pass
    def field_contributor_name():pass
    def field_contributor_occupation():pass
    def field_contributor_organization_name():pass
    def field_contributor_prefix():pass
    def field_contributor_state():pass
    def field_contributor_street_1():pass
    def field_contributor_street_2():pass
    def field_contributor_suffix():pass
    def field_contributor_zip_code():pass
    def field_contributor_zip():pass
    def field_controller_city():pass
    def field_controller_employer():pass
    def field_controller_first_name():pass
    def field_controller_last_name():pass
    def field_controller_middle_name():pass
    def field_controller_occupation():pass
    def field_controller_prefix():pass
    def field_controller_state():pass
    def field_controller_street_1():pass
    def field_controller_street_2():pass
    def field_controller_suffix():pass
    def field_controller_zip_code():pass
    def field_coordinated_expenditures():pass
    def field_c_other_political_committees_pacs():pass
    def field_c_other_political_committees():pass
    def field_coverage_from_date():pass
    def field_coverage_through_date():pass
    def field_credit_amount_this_draw():pass
    def field_creditor_city():pass
    def field_creditor_first_name():pass
    def field_creditor_last_name():pass
    def field_creditor_middle_name():pass
    def field_creditor_name():pass
    def field_creditor_organization_name():pass
    def field_creditor_prefix():pass
    def field_creditor_state():pass
    def field_creditor_street_1():pass
    def field_creditor_street_2():pass
    def field_creditor_suffix():pass
    def field_creditor_zip_code():pass
    def field_c_refund_other_political_committees():pass
    def field_c_total_loan_repayments_made():pass
    def field_c_total_loan_repayments():pass
    def field_c_total_loans():pass
    def field_custodian_city():pass
    def field_custodian_employer():pass
    def field_custodian_first_name():pass
    def field_custodian_last_name():pass
    def field_custodian_middle_name():pass
    def field_custodian_name():pass
    def field_custodian_occupation():pass
    def field_custodian_prefix():pass
    def field_custodian_state():pass
    def field_custodian_street_1():pass
    def field_custodian_street_2():pass
    def field_custodian_suffix():pass
    def field_custodian_telephone():pass
    def field_custodian_title():pass
    def field_custodian_zip_code():pass
    def field_date_day_after_general_election():pass
    def field_date_general_election():pass
    def field_date_notarized():pass
    def field_date_notary_commission_expires():pass
    def field_date_of_election():pass
    def field_date_public_distribution():pass
    def field_date_signed():pass
    def field_delaware():pass
    def field_deposit_acct_auth_date_presidential():pass
    def field_description():pass
    def field_designated_first_name():pass
    def field_designated_last_name():pass
    def field_designated_middle_name():pass
    def field_designated_prefix():pass
    def field_designated_suffix():pass
    def field_designating_committee_id_number():pass
    def field_designating_committee_name():pass
    def field_direct_candidate_support_activity():pass
    def field_direct_candidate_support():pass
    def field_direct_fundraising():pass
    def field_dist_of_columbia():pass
    def field_donation_aggregate_amount():pass
    def field_donation_amount():pass
    def field_donation_date():pass
    def field_donor_candidate_district():pass
    def field_donor_candidate_fec_id():pass
    def field_donor_candidate_first_name():pass
    def field_donor_candidate_last_name():pass
    def field_donor_candidate_middle_name():pass
    def field_donor_candidate_name():pass
    def field_donor_candidate_office():pass
    def field_donor_candidate_prefix():pass
    def field_donor_candidate_state():pass
    def field_donor_candidate_suffix():pass
    def field_donor_committee_fec_id():pass
    def field_donor_committee_name():pass
    def field_d_the_candidate():pass
    def field_d_total_contributions_refunds():pass
    def field_d_total_offsets_to_operating_expenditures():pass
    def field_effective_date():pass
    def field_ef_type():pass
    def field_election_code():pass
    def field_election_date():pass
    def field_election_district():pass
    def field_election_other_description():pass
    def field_election_state():pass
    def field_election_year():pass
    def field_end():pass
    def field_entity_type():pass
    def field_established_date():pass
    def field_estimated_value():pass
    def field_e_total_contributions_other_than_loans():pass
    def field_e_total_contributions():pass
    def field_event_activity_name():pass
    def field_event_type():pass
    def field_event_year_to_date():pass
    def field_exempt_activity():pass
    def field_exempt_legal_and_accounting_disbursements():pass
    def field_expenditure_amount():pass
    def field_expenditure_date():pass
    def field_expenditure_purpose_code():pass
    def field_expenditure_purpose_descrip():pass
    def field_expenditure_purpose_description():pass
    def field_extra_nonfederal_point():pass
    def field_F132():pass
    def field_F133():pass
    def field_F13():pass
    def field_F1M():pass
    def field_F1():pass
    def field_F1S():pass
    def field_F24():pass
    def field_F2():pass
    def field_F2S():pass
    def field_F3L():pass
#    def field_{F3L():pass
    def field_F3P31():pass
    def field_F3():pass
    def field_F3P():pass
    def field_F3PS():pass
    def field_F3S():pass
    def field_F3X():pass
    def field_F3Z():pass
    def field_F4():pass
    def field_F56():pass
    def field_F57():pass
    def field_F5():pass
    def field_F65():pass
    def field_F6():pass
    def field_F76():pass
    def field_F7():pass
    def field_F91():pass
    def field_F92():pass
    def field_F93():pass
    def field_F94():pass
    def field_F99():pass
    def field_F9():pass
    def field_f_basis_of_loan_description():pass
    def field_fec_candidate_id_number():pass
    def field_fec_committee_id_number():pass
    def field_fec_version():pass
    def field_federal_funds():pass
    def field_federal_percentage():pass
    def field_federal_percent():pass
    def field_federal_share():pass
    def field_fields():pass
    def field_fifth_candidate_contribution_date():pass
    def field_fifth_candidate_district():pass
    def field_fifth_candidate_fifth_name():pass
    def field_fifth_candidate_id_number():pass
    def field_fifth_candidate_last_name():pass
    def field_fifth_candidate_middle_name():pass
    def field_fifth_candidate_name():pass
    def field_fifth_candidate_office():pass
    def field_fifth_candidate_prefix():pass
    def field_fifth_candidate_state():pass
    def field_fifth_candidate_suffix():pass
    def field_fifty_first_contributor_date():pass
    def field_filer_code_description():pass
    def field_filer_code():pass
    def field_filer_committee_id_number():pass
    def field_first_candidate_contribution_date():pass
    def field_first_candidate_district():pass
    def field_first_candidate_first_name():pass
    def field_first_candidate_id_number():pass
    def field_first_candidate_last_name():pass
    def field_first_candidate_middle_name():pass
    def field_first_candidate_name():pass
    def field_first_candidate_office():pass
    def field_first_candidate_prefix():pass
    def field_first_candidate_state():pass
    def field_first_candidate_suffix():pass
    def field_flat_minimum_federal_percentage():pass
    def field_florida():pass
    def field_form_type():pass
    def field_fourth_candidate_contribution_date():pass
    def field_fourth_candidate_district():pass
    def field_fourth_candidate_fourth_name():pass
    def field_fourth_candidate_id_number():pass
    def field_fourth_candidate_last_name():pass
    def field_fourth_candidate_middle_name():pass
    def field_fourth_candidate_name():pass
    def field_fourth_candidate_office():pass
    def field_fourth_candidate_prefix():pass
    def field_fourth_candidate_state():pass
    def field_fourth_candidate_suffix():pass
    def field_fundraising_activity():pass
    def field_fundraising_disbursements():pass
    def field_future_income():pass
    def field_general_election():pass
    def field_general_personal_funds_declared():pass
    def field_generic_campaign_activity():pass
    def field_generic_campaign_amount():pass
    def field_generic_voter_drive_activity():pass
    def field_generic_voter_drive_ratio_applies():pass
    def field_georgia():pass
    def field_gotv_activity():pass
    def field_gotv_amount():pass
    def field_guam():pass
    def field_guaranteed_amount():pass
    def field_guarantor_city():pass
    def field_guarantor_employer():pass
    def field_guarantor_first_name():pass
    def field_guarantor_last_name():pass
    def field_guarantor_middle_name():pass
    def field_guarantor_name():pass
    def field_guarantor_occupation():pass
    def field_guarantor_prefix():pass
    def field_guarantor_state():pass
    def field_guarantor_street_1():pass
    def field_guarantor_street_2():pass
    def field_guarantor_suffix():pass
    def field_guarantor_zip_code():pass
    def field_hawaii():pass
    def field_Header():pass
    def field_house_senate_party_committees_actual_federal_candidate_support():pass
    def field_house_senate_party_committees_actual_nonfederal_candidate_support():pass
    def field_house_senate_party_committees_minimum_federal_percentage():pass
    def field_house_senate_party_committees_percentage_actual_federal():pass
    def field_house_senate_party_committees_percentage_federal_candidate_support():pass
    def field_house_senate_party_committees_percentage_nonfederal_candidate_support():pass
    def field_idaho():pass
    def field_illinois():pass
    def field_increased_limit_code():pass
    def field_increased_limit():pass
    def field_incurred_amount_this_period():pass
    def field_indiana():pass
    def field_individual_employer():pass
    def field_individual_first_name():pass
    def field_individual_last_name():pass
    def field_individual_middle_name():pass
    def field_individual_occupation():pass
    def field_individual_prefix():pass
    def field_individual_suffix():pass
    def field_ind_name_as_signed():pass
    def field_ind_name_notary():pass
    def field_iowa():pass
    def field_item_contribution_aquired_date():pass
    def field_item_description():pass
    def field_item_fair_market_value():pass
    def field_kansas():pass
    def field_kentucky():pass
#    def field_layout)():pass
    def field_leadership_pac():pass
    def field_lender_candidate_district():pass
    def field_lender_candidate_first_name():pass
    def field_lender_candidate_id_number():pass
    def field_lender_candidate_last_name():pass
    def field_lender_candidate_middle_nm():pass
    def field_lender_candidate_name():pass
    def field_lender_candidate_office():pass
    def field_lender_candidate_prefix():pass
    def field_lender_candidate_state():pass
    def field_lender_candidate_suffix():pass
    def field_lender_city():pass
    def field_lender_committee_id_number():pass
    def field_lender_first_name():pass
    def field_lender_last_name():pass
    def field_lender_middle_name():pass
    def field_lender_name():pass
    def field_lender_organization_name():pass
    def field_lender_prefix():pass
    def field_lender_state():pass
    def field_lender_street_1():pass
    def field_lender_street_2():pass
    def field_lender_suffix():pass
    def field_lender_zip_code():pass
    def field_LEVIN():pass
    def field_levin_share():pass
    def field_line():pass
    def field_loan_amount_original():pass
    def field_loan_amount():pass
    def field_loan_balance():pass
    def field_loan_due_date():pass
    def field_loan_due_date_terms():pass
    def field_loan_inccured_date_original():pass
    def field_loan_incurred_date():pass
    def field_loan_incurred_date_terms():pass
    def field_loan_interest_rate():pass
    def field_loan_interest_rate_terms():pass
    def field_loan_payment_to_date():pass
    def field_loan_restructured():pass
    def field_lobbyist_registrant_pac_2():pass
    def field_lobbyist_registrant_pac():pass
    def field_louisiana():pass
    def field_maine():pass
    def field_maryland():pass
    def field_massachusetts():pass
    def field_memo_code():pass
    def field_memo_text_description():pass
    def field_memo_text():pass
    def field_michigan():pass
    def field_minnesota():pass
    def field_mississippi():pass
    def field_missouri():pass
    def field_montana():pass
    def field_name_delim():pass
    def field_national_party_committee_percentage():pass
    def field_nebraska():pass
    def field_net_contributions():pass
    def field_net_donations():pass
    def field_net_expenditures():pass
    def field_nevada():pass
    def field_new_hampshire():pass
    def field_new_jersey():pass
    def field_new_mexico():pass
#    def field_(New():pass
    def field_new_york():pass
    def field_nonfederal_percent():pass
    def field_nonfederal_share():pass
    def field_non_presidential_non_senate_election_year():pass
    def field_north_carolina():pass
    def field_north_dakota():pass
    def field_notary_name():pass
    def field_offsets_to_operating_expenditures():pass
    def field_of():pass
    def field_ohio():pass
    def field_oklahoma():pass
    def field_operating_expenditures():pass
    def field_oregon():pass
    def field_organization_name():pass
    def field_organization_type():pass
    def field_original_amendment_date():pass
    def field_original_registration_date():pass
    def field_other_disbursements():pass
    def field_other_receipts():pass
    def field_others_liable():pass
    def field_party_code():pass
    def field_party_type():pass
#    def field_-():pass
#    def field_&():pass
    def field_payee_candidate_district():pass
    def field_payee_candidate_first_name():pass
    def field_payee_candidate_id_number():pass
    def field_payee_candidate_last_name():pass
    def field_payee_candidate_middle_name():pass
    def field_payee_candidate_name():pass
    def field_payee_candidate_office():pass
    def field_payee_candidate_prefix():pass
    def field_payee_candidate_state():pass
    def field_payee_candidate_suffix():pass
    def field_payee_city():pass
    def field_payee_cmtte_fec_id_number():pass
    def field_payee_committee_id_number():pass
    def field_payee_employer():pass
    def field_payee_first_name():pass
    def field_payee_last_name():pass
    def field_payee_middle_name():pass
    def field_payee_name():pass
    def field_payee_occupation():pass
    def field_payee_organization_name():pass
    def field_payee_prefix():pass
    def field_payee_state():pass
    def field_payee_street_1():pass
    def field_payee_street_2():pass
    def field_payee_suffix():pass
    def field_payee_zip_code():pass
    def field_payment_amount_this_period():pass
    def field_pennsylvania():pass
    def field_perfected_interest():pass
    def field_personal_funds():pass
    def field_person_completing_first_name():pass
    def field_person_completing_last_name():pass
    def field_person_completing_middle_name():pass
    def field_person_completing_name():pass
    def field_person_completing_prefix():pass
    def field_person_completing_suffix():pass
    def field_person_designated_first_name():pass
    def field_person_designated_last_name():pass
    def field_person_designated_middle_name():pass
    def field_person_designated_name():pass
    def field_person_designated_prefix():pass
    def field_person_designated_suffix():pass
    def field_person_designated_title():pass
    def field_presidential_only_election_year():pass
    def field_presidential_senate_election_year():pass
    def field_primary_election():pass
    def field_primary_personal_funds_declared():pass
    def field_public_communications_party_activity():pass
    def field_public_communications_referencing_party_ratio_applies():pass
    def field_puerto_rico():pass
    def field_purpose_of_debt_or_obligation():pass
    def field_qualified_committee():pass
    def field_qualified_non_profit():pass
    def field_qualified_nonprofit():pass
    def field_quarterly_monthly_bundled_contributions():pass
    def field_ratio_code():pass
    def field_receipt_date():pass
    def field_receipt_line_number():pass
    def field_record_id_number():pass
    def field_record_type():pass
    def field_reference_code():pass
    def field_reference_to_si_or_sl_system_code_that_identifies_the_account():pass
    def field_refund_amount():pass
    def field_refund_date():pass
    def field_refund_or_disposal_of_excess():pass
    def field_report_code():pass
    def field_report_id():pass
    def field_report_number():pass
    def field_REPORT():pass
    def field_report_pgi():pass
    def field_report_type():pass
    def field_requirements_met_date():pass
    def field_rhode_island():pass
    def field_runoff_election():pass
    def field_SchA():pass
    def field_SchB():pass
    def field_SchC1():pass
    def field_SchC2():pass
    def field_SchC():pass
    def field_SchD():pass
    def field_SchE():pass
    def field_SchF():pass
    def field_SchH1():pass
    def field_SchH2():pass
    def field_SchH3():pass
    def field_SchH4():pass
    def field_SchH5():pass
    def field_SchH6():pass
    def field_SchI():pass
    def field_SchL():pass
    def field_second_candidate_contribution_date():pass
    def field_second_candidate_district():pass
    def field_second_candidate_id_number():pass
    def field_second_candidate_last_name():pass
    def field_second_candidate_middle_name():pass
    def field_second_candidate_name():pass
    def field_second_candidate_office():pass
    def field_second_candidate_prefix():pass
    def field_second_candidate_second_name():pass
    def field_second_candidate_state():pass
    def field_second_candidate_suffix():pass
    def field_secured():pass
    def field_segregated_bank_account():pass
    def field_semi_annual_bundled_contributions():pass
#    def field_Semi-annual():pass
    def field_semi_annual_period_jan_june():pass
    def field_semi_annual_period_jul_dec():pass
    def field_semi_annual_period():pass
    def field_semi_annual_refunded_bundled_amt():pass
    def field_senate_only_election_year():pass
    def field_signature_first_name():pass
    def field_signature_last_name():pass
    def field_signature_middle_name():pass
    def field_signature_name():pass
    def field_signature_prefix():pass
    def field_signature_suffix():pass
    def field_signer_first_name():pass
    def field_signer_last_name():pass
    def field_signer_middle_name():pass
    def field_signer_prefix():pass
    def field_signer_suffix():pass
    def field_soft_name():pass
    def field_soft_ver():pass
    def field_south_carolina():pass
    def field_south_dakota():pass
    def field_special_election():pass
    def field_state_of_election():pass
    def field_state():pass
    def field_street_1():pass
    def field_street_2():pass
    def field_subordinate_city():pass
    def field_subordinate_committee_id_number():pass
    def field_subordinate_committee_name():pass
    def field_subordinate_state():pass
    def field_subordinate_street_1():pass
    def field_subordinate_street_2():pass
    def field_subordinate_zip_code():pass
    def field_subtotal_federal():pass
    def field_subtotal():pass
    def field_support_oppose_code():pass
    def field_tennessee():pass
    def field_texas():pass
    def field_text_code():pass
    def field_TEXT():pass
    def field_third_candidate_contribution_date():pass
    def field_third_candidate_district():pass
    def field_third_candidate_id_number():pass
    def field_third_candidate_last_name():pass
    def field_third_candidate_middle_name():pass
    def field_third_candidate_name():pass
    def field_third_candidate_office():pass
    def field_third_candidate_prefix():pass
    def field_third_candidate_state():pass
    def field_third_candidate_suffix():pass
    def field_third_candidate_third_name():pass
    def field_this():pass
    def field_to():pass
    def field_total_amount():pass
    def field_total_amount_transferred():pass
    def field_total_balance():pass
    def field_total_contribution():pass
    def field_total_costs():pass
    def field_total_disbursements():pass
    def field_total_donations_accepted():pass
    def field_total_donations():pass
    def field_total_donations_refunded():pass
    def field_total_independent_expenditure():pass
    def field_total_points():pass
    def field_total_receipts():pass
    def field_totals():pass
    def field_TOTALS():pass
    def field_transaction_code():pass
    def field_transaction_description():pass
    def field_transaction_id_number():pass
    def field_transaction_id():pass
    def field_transaction_type():pass
    def field_transferred_amount():pass
    def field_transfers_from_aff_other_party_committees():pass
    def field_transfers_from_other_auth_committees():pass
    def field_transfers_to_other_auth_committees():pass
    def field_transfers_to_other_authorized_committees():pass
    def field_treasurer_city():pass
    def field_treasurer_first_name():pass
    def field_treasurer_last_name():pass
    def field_treasurer_middle_name():pass
    def field_treasurer_name():pass
    def field_treasurer_prefix():pass
    def field_treasurer_state():pass
    def field_treasurer_street_1():pass
    def field_treasurer_street_2():pass
    def field_treasurer_suffix():pass
    def field_treasurer_telephone():pass
    def field_treasurer_title():pass
    def field_treasurer_zip_code():pass
    def field_utah():pass
    def field_vermont():pass
    def field_virginia():pass
    def field_virgin_islands():pass
    def field_voter_id_activity():pass
    def field_voter_id_amount():pass
    def field_voter_registration_activity():pass
    def field_voter_registration_amount():pass
    def field_washington():pass
    def field_west_virginia():pass
    def field_wisconsin():pass
    def field_wyoming():pass
#    def field_YEAR-TO-DATE():pass
    def field_YTD():pass
    def field_zip_code():pass

    def __init__(self) :
        self.FILING_VERSIONS   = ["8.0", "7.0", "6.4", "6.3", "6.2", "6.1",
                                  "5.3", "5.2", "5.1", "5.0", "3"]
        self.BASE_ROW_TYPES    = ["HDR", "F1", "F13", "F132", "F133", "F1M", "F2", "F24", "F3", "F3L", "F3P", "F3P31", "F3PS", 
                                  "F3S", "F3X", "F4", "F5", "F56", "F57", "F6", "F65", "F7", "F76", "F9", "F91", "F92", "F93", 
                                  "F94", "F99", "H1", "H2", "H3", "H4", "H5", "H6",
                                  "SchA", "SchB", "SchC", "SchC1", "SchC2", "SchD", "SchE", "SchF", "SchL", "TEXT"]
        
        ###
        self.ROW_TYPES_REGEX = {
            'hdr'   : r'^hdr$',
            'f1'    : r'^f1',
            'f13'   : r'^f13[an]',
            'f132'  : r'^f132',
            'f133'  : r'^f133',
            'f1m'   : r'(^f1m[^a|n])',
            'f2'    : r'(^f2$)|(^f2[^4])',
            'f24'   : r'(^f24$)|(^f24[an])',
            'f3'    : r'^f3[a|n|t]',
            'f3l'   : r'^f3l[a|n]',
            'f3p'   : r'(^f3p$)|(^f3p[^s|3])',
            'f3s'   : r'^f3s',
            'f3p31' : r'^f3p31',
            'f3ps'  : r'^f3ps',
            'f3x'   : r'(^f3x$)|(^f3x[ant])',
            'f4'    : r'^f4[na]',
            'f5'    : r'^f5[na]',
            'f56'   : r'^f56',
            'f57'   : r'^f57',
            'f6'    : r'(^f6$)|(^f6[an])',
            'f65'   : r'^f65',
            'f7'    : r'^f7[na]',
            'f76'   : r'^f76',
            'f9'    : r'^f9',
            'f91'   : r'^f91',
            'f92'   : r'^f92',
            'f93'   : r'^f93',
            'f94'   : r'^f94',
            'f99'   : r'^f99',
            'h1'    : r'^h1',
            'h2'    : r'^h2',
            'h3'    : r'^h3',
            'h4'    : r'^h4',
            'h5'    : r'^h5',
            'h6'    : r'^h6',
            'sa'    : r'^sa',
            'sb'    : r'^sb',
            'sc'    : r'^sc[^1-2]',
            'sc1'   : r'^sc1',
            'sc2'   : r'^sc2',
            'sd'    : r'^sd',
            'se'    : r'^se',
            'sf'    : r'^sf',
            'sl'    : r'^sl',
            'text'  : r'^text',
        }

        self.ROW_TYPES = {
            "HDR"    : self.RowTypes_hdr,
            "F1"     : self.RowTypes_f1,
            "F13"    : self.RowTypes_f13,
            "F132"   : self.RowTypes_f132,
            "F133"   : self.RowTypes_f133,
            "F1M"    : self.RowTypes_f1m,
            "F2"     : self.RowTypes_f2,
            "F24"    : self.RowTypes_f24,
            "F3"     : self.RowTypes_f3,
            "F3L"    : self.RowTypes_f3l,
            "F3P"    : self.RowTypes_f3p,
            "F3S"    : self.RowTypes_f3s,
            "F3P31"  : self.RowTypes_f3p31,
            "F3PS"   : self.RowTypes_f3ps,
            "F3X"    : self.RowTypes_f3x,
            "F4"     : self.RowTypes_f4,
            "F5"     : self.RowTypes_f5,
            "F56"    : self.RowTypes_f56,
            "F57"    : self.RowTypes_f57,
            "F6"     : self.RowTypes_f6,
            "F65"    : self.RowTypes_f65,
            "F7"     : self.RowTypes_f7,
            "F76"    : self.RowTypes_f76,
            "F9"     : self.RowTypes_f9,
            "F91"    : self.RowTypes_f91,
            "F92"    : self.RowTypes_f92,
            "F93"    : self.RowTypes_f93,
            "F94"    : self.RowTypes_f94,
            "F99"    : self.RowTypes_f99,
            "H1"     : self.RowTypes_h1,
            "H2"     : self.RowTypes_h2,
            "H3"     : self.RowTypes_h3,
            "H4"     : self.RowTypes_h4,
            "H5"     : self.RowTypes_h5,
            "H6"     : self.RowTypes_h6,
            "SchA"   : self.RowTypes_sa,
            "SchB"   : self.RowTypes_sb,
            "SchC"   : self.RowTypes_sc,
            "SchC1"  : self.RowTypes_sc1,
            "SchC2"  : self.RowTypes_sc2,
            "SchD"   : self.RowTypes_sd,
            "SchE"   : self.RowTypes_se,
            "SchF"   : self.RowTypes_sf,
            "SchL"   : self.RowTypes_sl,
            "TEXT"   : self.RowTypes_text,  
        }


        RENDERED_MAPS = {
            "^hdr$" : {
                '^[6-8]' : [ self.field_record_type, self.field_ef_type, self.field_fec_version, self.field_soft_name, self.field_soft_ver, self.field_report_id, self.field_report_number, self.field_comment],
                '^[3-5]' : [ self.field_record_type, self.field_ef_type, self.field_fec_version, self.field_soft_name, self.field_soft_ver, self.field_name_delim, self.field_report_id, self.field_report_number, self.field_comment],
            },
            "^f1" : {
                '^8.0|7.0|6.4' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_change_of_committee_name, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_committee_email, self.field_committee_email, self.field_change_of_committee_url, self.field_committee_url, self.field_effective_date, self.field_signature_last_name, self.field_signature_first_name, self.field_signature_middle_name, self.field_signature_prefix, self.field_signature_suffix, self.field_date_signed, self.field_committee_type, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_party_code, self.field_party_type, self.field_organization_type, self.field_lobbyist_registrant_pac, self.field_lobbyist_registrant_pac_2, self.field_leadership_pac, self.field_affiliated_committee_id_number, self.field_affiliated_committee_name, self.field_affiliated_candidate_id_number, self.field_affiliated_last_name, self.field_affiliated_first_name, self.field_affiliated_middle_name, self.field_affiliated_prefix, self.field_affiliated_suffix, self.field_affiliated_street_1, self.field_affiliated_street_2, self.field_affiliated_city, self.field_affiliated_state, self.field_affiliated_zip_code, self.field_affiliated_relationship_code, self.field_custodian_last_name, self.field_custodian_first_name, self.field_custodian_middle_name, self.field_custodian_prefix, self.field_custodian_suffix, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_title, self.field_custodian_telephone, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_treasurer_street_1, self.field_treasurer_street_2, self.field_treasurer_city, self.field_treasurer_state, self.field_treasurer_zip_code, self.field_treasurer_title, self.field_treasurer_telephone, self.field_agent_last_name, self.field_agent_first_name, self.field_agent_middle_name, self.field_agent_prefix, self.field_agent_suffix, self.field_agent_street_1, self.field_agent_street_2, self.field_agent_city, self.field_agent_state, self.field_agent_zip_code, self.field_agent_title, self.field_agent_telephone, self.field_bank_name, self.field_bank_street_1, self.field_bank_street_2, self.field_bank_city, self.field_bank_state, self.field_bank_zip_code, self.field_bank2_name, self.field_bank2_street_1, self.field_bank2_street_2, self.field_bank2_city, self.field_bank2_state, self.field_bank2_zip_code],
                '^6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_change_of_committee_name, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_committee_email, self.field_committee_email, self.field_change_of_committee_url, self.field_committee_url, self.field_effective_date, self.field_signature_last_name, self.field_signature_first_name, self.field_signature_middle_name, self.field_signature_prefix, self.field_signature_suffix, self.field_date_signed, self.field_committee_type, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_party_code, self.field_party_type, self.field_organization_type, self.field_lobbyist_registrant_pac, self.field_lobbyist_registrant_pac_2, self.field_leadership_pac, self.field_affiliated_committee_id_number, self.field_affiliated_committee_name, self.field_affiliated_candidate_id_number, self.field_affiliated_last_name, self.field_affiliated_first_name, self.field_affiliated_middle_name, self.field_affiliated_prefix, self.field_affiliated_suffix, self.field_affiliated_street_1, self.field_affiliated_street_2, self.field_affiliated_city, self.field_affiliated_state, self.field_affiliated_zip_code, self.field_affiliated_relationship_code, self.field_custodian_last_name, self.field_custodian_first_name, self.field_custodian_middle_name, self.field_custodian_prefix, self.field_custodian_suffix, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_title, self.field_custodian_telephone, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_treasurer_street_1, self.field_treasurer_street_2, self.field_treasurer_city, self.field_treasurer_state, self.field_treasurer_zip_code, self.field_treasurer_title, self.field_treasurer_telephone, self.field_agent_last_name, self.field_agent_first_name, self.field_agent_middle_name, self.field_agent_prefix, self.field_agent_suffix, self.field_agent_street_1, self.field_agent_street_2, self.field_agent_city, self.field_agent_state, self.field_agent_zip_code, self.field_agent_title, self.field_agent_telephone, self.field_bank_name, self.field_bank_street_1, self.field_bank_street_2, self.field_bank_city, self.field_bank_state, self.field_bank_zip_code, self.field_bank2_name, self.field_bank2_street_1, self.field_bank2_street_2, self.field_bank2_city, self.field_bank2_state, self.field_bank2_zip_code],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_effective_date, self.field_change_of_committee_name, self.field_change_of_address, self.field_committee_type, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_party_code, self.field_party_type, self.field_affiliated_committee_id_number, self.field_affiliated_committee_name, self.field_affiliated_street_1, self.field_affiliated_street_2, self.field_affiliated_city, self.field_affiliated_state, self.field_affiliated_zip_code, self.field_affiliated_relationship_code, self.field_organization_type, self.field_custodian_name, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_title, self.field_custodian_telephone, self.field_treasurer_name, self.field_treasurer_street_1, self.field_treasurer_street_2, self.field_treasurer_city, self.field_treasurer_state, self.field_treasurer_zip_code, self.field_treasurer_title, self.field_treasurer_telephone, self.field_agent_name, self.field_agent_street_1, self.field_agent_street_2, self.field_agent_city, self.field_agent_state, self.field_agent_zip_code, self.field_agent_title, self.field_agent_telephone, self.field_bank_name, self.field_bank_street_1, self.field_bank_street_2, self.field_bank_city, self.field_bank_state, self.field_bank_zip_code, self.field_signature_name, self.field_date_signed, self.field_committee_email, self.field_committee_url, self.field_committee_fax_number],
              '^3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_effective_date, self.field_change_of_committee_name, self.field_change_of_address, self.field_committee_type, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_party_code, self.field_party_type, self.field_affiliated_committee_id_number, self.field_affiliated_committee_name, self.field_affiliated_street_1, self.field_affiliated_street_2, self.field_affiliated_city, self.field_affiliated_state, self.field_affiliated_zip_code, self.field_affiliated_relationship_code, self.field_organization_type, self.field_custodian_name, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_title, self.field_custodian_telephone, self.field_treasurer_name, self.field_treasurer_street_1, self.field_treasurer_street_2, self.field_treasurer_city, self.field_treasurer_state, self.field_treasurer_zip_code, self.field_treasurer_title, self.field_treasurer_telephone, self.field_agent_name, self.field_agent_street_1, self.field_agent_street_2, self.field_agent_city, self.field_agent_state, self.field_agent_zip_code, self.field_agent_title, self.field_agent_telephone, self.field_bank_name, self.field_bank_street_1, self.field_bank_street_2, self.field_bank_city, self.field_bank_state, self.field_bank_zip_code, self.field_signature_name, self.field_date_signed, self.field_committee_email, self.field_committee_url],
            },
            "^f13[an]" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_report_code, self.field_amendment_date, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_donations_accepted, self.field_total_donations_refunded, self.field_net_donations, self.field_designated_last_name, self.field_designated_first_name, self.field_designated_middle_name, self.field_designated_prefix, self.field_designated_suffix, self.field_date_signed],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_report_code, self.field_amendment_date, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_donations_accepted, self.field_total_donations_refunded, self.field_net_donations, self.field_designated_last_name, self.field_designated_first_name, self.field_designated_middle_name, self.field_designated_prefix, self.field_designated_suffix, self.field_date_signed],
            },
            "^f132" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip, self.field_donation_date, self.field_donation_amount, self.field_donation_aggregate_amount, self.field_memo_code, self.field_memo_text_description],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip, self.field_donation_date, self.field_donation_amount, self.field_donation_aggregate_amount, None , self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^f133" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip, self.field_refund_date, self.field_refund_amount, self.field_memo_code, self.field_memo_text_description],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip, self.field_refund_date, self.field_refund_amount, None, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "(^f1m[^a|n])" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_committee_type, self.field_affiliated_date_f1_filed, self.field_affiliated_committee_id_number, self.field_affiliated_committee_name, self.field_first_candidate_id_number, self.field_first_candidate_last_name, self.field_first_candidate_first_name, self.field_first_candidate_middle_name, self.field_first_candidate_prefix, self.field_first_candidate_suffix, self.field_first_candidate_office, self.field_first_candidate_state, self.field_first_candidate_district, self.field_first_candidate_contribution_date, self.field_second_candidate_id_number, self.field_second_candidate_last_name, self.field_second_candidate_second_name, self.field_second_candidate_middle_name, self.field_second_candidate_prefix, self.field_second_candidate_suffix, self.field_second_candidate_office, self.field_second_candidate_state, self.field_second_candidate_district, self.field_second_candidate_contribution_date, self.field_third_candidate_id_number, self.field_third_candidate_last_name, self.field_third_candidate_third_name, self.field_third_candidate_middle_name, self.field_third_candidate_prefix, self.field_third_candidate_suffix, self.field_third_candidate_office, self.field_third_candidate_state, self.field_third_candidate_district, self.field_third_candidate_contribution_date, self.field_fourth_candidate_id_number, self.field_fourth_candidate_last_name, self.field_fourth_candidate_fourth_name, self.field_fourth_candidate_middle_name, self.field_fourth_candidate_prefix, self.field_fourth_candidate_suffix, self.field_fourth_candidate_office, self.field_fourth_candidate_state, self.field_fourth_candidate_district, self.field_fourth_candidate_contribution_date, self.field_fifth_candidate_id_number, self.field_fifth_candidate_last_name, self.field_fifth_candidate_fifth_name, self.field_fifth_candidate_middle_name, self.field_fifth_candidate_prefix, self.field_fifth_candidate_suffix, self.field_fifth_candidate_office, self.field_fifth_candidate_state, self.field_fifth_candidate_district, self.field_fifth_candidate_contribution_date, self.field_fifty_first_contributor_date, self.field_original_registration_date, self.field_requirements_met_date, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_committee_type, self.field_affiliated_date_f1_filed, self.field_affiliated_committee_id_number, self.field_affiliated_committee_name, self.field_first_candidate_id_number, self.field_first_candidate_name, self.field_first_candidate_office, self.field_first_candidate_state, self.field_first_candidate_district, self.field_first_candidate_contribution_date, self.field_second_candidate_id_number, self.field_second_candidate_name, self.field_second_candidate_office, self.field_second_candidate_state, self.field_second_candidate_district, self.field_second_candidate_contribution_date, self.field_third_candidate_id_number, self.field_third_candidate_name, self.field_third_candidate_office, self.field_third_candidate_state, self.field_third_candidate_district, self.field_third_candidate_contribution_date, self.field_fourth_candidate_id_number, self.field_fourth_candidate_name, self.field_fourth_candidate_office, self.field_fourth_candidate_state, self.field_fourth_candidate_district, self.field_fourth_candidate_contribution_date, self.field_fifth_candidate_id_number, self.field_fifth_candidate_name, self.field_fifth_candidate_office, self.field_fifth_candidate_state, self.field_fifth_candidate_district, self.field_fifth_candidate_contribution_date, self.field_fifty_first_contributor_date, self.field_original_registration_date, self.field_requirements_met_date, self.field_treasurer_name, self.field_date_signed],
            },
            "(^f2$)|(^f2[^4])" : {
              '^8.0|7.0|6.4' : [ self.field_form_type, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_change_of_address, self.field_candidate_street_1, self.field_candidate_street_2, self.field_candidate_city, self.field_candidate_state, self.field_candidate_zip_code, self.field_candidate_party_code, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_year, self.field_committee_id_number, self.field_committee_name, self.field_committee_street_1, self.field_committee_street_2, self.field_committee_city, self.field_committee_state, self.field_committee_zip_code, self.field_authorized_committee_id_number, self.field_authorized_committee_name, self.field_authorized_committee_street_1, self.field_authorized_committee_street_2, self.field_authorized_committee_city, self.field_authorized_committee_state, self.field_authorized_committee_zip_code, self.field_candidate_signature_last_name, self.field_candidate_signature_first_name, self.field_candidate_signature_middle_name, self.field_candidate_signature_prefix, self.field_candidate_signature_suffix, self.field_date_signed],
              '^6.3|6.2|6.1' : [ self.field_form_type, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_change_of_address, self.field_candidate_street_1, self.field_candidate_street_2, self.field_candidate_city, self.field_candidate_state, self.field_candidate_zip_code, self.field_candidate_party_code, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_year, self.field_committee_id_number, self.field_committee_name, self.field_committee_street_1, self.field_committee_street_2, self.field_committee_city, self.field_committee_state, self.field_committee_zip_code, self.field_authorized_committee_id_number, self.field_authorized_committee_name, self.field_authorized_committee_street_1, self.field_authorized_committee_street_2, self.field_authorized_committee_city, self.field_authorized_committee_state, self.field_authorized_committee_zip_code, self.field_primary_personal_funds_declared, self.field_general_personal_funds_declared, self.field_candidate_signature_last_name, self.field_candidate_signature_first_name, self.field_candidate_signature_middle_name, self.field_candidate_signature_prefix, self.field_candidate_signature_suffix, self.field_date_signed],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_street_1, self.field_candidate_street_2, self.field_candidate_city, self.field_candidate_state, self.field_candidate_zip_code, self.field_candidate_party_code, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_year, self.field_committee_id_number, self.field_committee_name, self.field_committee_street_1, self.field_committee_street_2, self.field_committee_city, self.field_committee_state, self.field_committee_zip_code, self.field_authorized_committee_id_number, self.field_authorized_committee_name, self.field_authorized_committee_street_1, self.field_authorized_committee_street_2, self.field_authorized_committee_city, self.field_authorized_committee_state, self.field_authorized_committee_zip_code, self.field_candidate_signature_name, self.field_date_signed, self.field_primary_personal_funds_declared, self.field_general_personal_funds_declared, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix],
              '^3.0' : [ self.field_form_type, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_street_1, self.field_candidate_street_2, self.field_candidate_city, self.field_candidate_state, self.field_candidate_zip_code, self.field_candidate_party_code, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_year, self.field_committee_id_number, self.field_committee_name, self.field_committee_street_1, self.field_committee_street_2, self.field_committee_city, self.field_committee_state, self.field_committee_zip_code, self.field_authorized_committee_id_number, self.field_authorized_committee_name, self.field_authorized_committee_street_1, self.field_authorized_committee_street_2, self.field_authorized_committee_city, self.field_authorized_committee_state, self.field_authorized_committee_zip_code, self.field_candidate_signature_name, self.field_date_signed],
            },
            "(^f24$)|(^f24[an])" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_report_type, self.field_original_amendment_date, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed],
              '^7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_report_type, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed],
              '^5.0|5.1|5.2|5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, None, self.field_date_signed, self.field_report_type],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, None, self.field_date_signed],
            },
            "^f3[a|n|t]" : {
              '^8.0|7.0|6.4' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_election_state, self.field_election_district, self.field_report_code, self.field_election_code, self.field_election_date, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_col_a_total_contributions_no_loans, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_operating_expenditures, self.field_col_a_total_offset_to_operating_expenditures, self.field_col_a_net_operating_expenditures, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individual_contributions_itemized, self.field_col_a_individual_contributions_unitemized, self.field_col_a_total_individual_contributions, self.field_col_a_political_party_contributions, self.field_col_a_pac_contributions, self.field_col_a_candidate_contributions, self.field_col_a_total_contributions, self.field_col_a_transfers_from_authorized, self.field_col_a_candidate_loans, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_offset_to_operating_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_authorized, self.field_col_a_candidate_loan_repayments, self.field_col_a_other_loan_repayments, self.field_col_a_total_loan_repayments, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_cash_beginning_reporting_period, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_receipts_period, self.field_col_a_cash_on_hand_close, self.field_col_b_total_contributions_no_loans, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_operating_expenditures, self.field_col_b_total_offset_to_operating_expenditures, self.field_col_b_net_operating_expenditures, self.field_col_b_individual_contributions_itemized, self.field_col_b_individual_contributions_unitemized, self.field_col_b_total_individual_contributions, self.field_col_b_political_party_contributions, self.field_col_b_pac_contributions, self.field_col_b_candidate_contributions, self.field_col_b_total_contributions, self.field_col_b_transfers_from_authorized, self.field_col_b_candidate_loans, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_offset_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_authorized, self.field_col_b_candidate_loan_repayments, self.field_col_b_other_loan_repayments, self.field_col_b_total_loan_repayments, self.field_col_b_refunds_to_individuals, self.field_col_b_refunds_to_party_committees, self.field_col_b_refunds_to_other_committees, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements],
              '^6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_election_state, self.field_election_district, self.field_election_date, self.field_election_code, None, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_report_type, self.field_col_a_total_contributions_no_loans, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_operating_expenditures, self.field_col_a_total_offset_to_operating_expenditures, self.field_col_a_net_operating_expenditures, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individual_contributions_itemized, self.field_col_a_individual_contributions_unitemized, self.field_col_a_total_individual_contributions, self.field_col_a_political_party_contributions, self.field_col_a_pac_contributions, self.field_col_a_candidate_contributions, self.field_col_a_total_contributions, self.field_col_a_transfers_from_authorized, self.field_col_a_candidate_loans, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_offset_to_operating_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_authorized, self.field_col_a_candidate_loan_repayments, None, self.field_col_a_total_loan_repayments, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_cash_beginning_reporting_period, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_receipts_period, self.field_col_a_cash_on_hand_close, self.field_col_b_total_contributions_no_loans, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_operating_expenditures, self.field_col_b_total_offset_to_operating_expenditures, self.field_col_b_net_operating_expenditures, self.field_col_b_individual_contributions_itemized, self.field_col_b_individual_contributions_unitemized, self.field_col_b_total_individual_contributions, self.field_col_b_political_party_contributions, self.field_col_b_pac_contributions, self.field_col_b_candidate_contributions, self.field_col_b_total_contributions, self.field_col_b_transfers_from_authorized, self.field_col_b_candidate_loans, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_offset_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_authorized, self.field_col_b_candidate_loan_repayments, None, self.field_col_b_total_loan_repayments, self.field_col_b_refunds_to_individuals, None, None, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_gross_receipts_authorized_primary, self.field_col_b_aggregate_personal_funds_primary, self.field_col_b_gross_receipts_minus_personal_funds_primary, self.field_col_b_gross_receipts_authorized_general, self.field_col_b_aggregate_personal_funds_general, self.field_col_b_gross_receipts_minus_personal_funds_general],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_election_state, self.field_election_district, self.field_report_code, self.field_election_code, self.field_election_date, self.field_state_of_election, self.field_primary_election, self.field_general_election, self.field_special_election, self.field_runoff_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_total_contributions_no_loans, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_operating_expenditures, self.field_col_a_total_offset_to_operating_expenditures, self.field_col_a_net_operating_expenditures, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individual_contributions_itemized, self.field_col_a_individual_contributions_unitemized, self.field_col_a_total_individual_contributions, self.field_col_a_political_party_contributions, self.field_col_a_pac_contributions, self.field_col_a_candidate_contributions, self.field_col_a_total_contributions, self.field_col_a_transfers_from_authorized, self.field_col_a_candidate_loans, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_offset_to_operating_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_authorized, self.field_col_a_candidate_loan_repayments, None, self.field_col_a_total_loan_repayments, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_cash_beginning_reporting_period, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_receipts_period, self.field_col_a_cash_on_hand_close, self.field_col_b_total_contributions_no_loans, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_operating_expenditures, self.field_col_b_total_offset_to_operating_expenditures, self.field_col_b_net_operating_expenditures, self.field_col_b_individual_contributions_itemized, self.field_col_b_individual_contributions_unitemized, self.field_col_b_total_individual_contributions, self.field_col_b_political_party_contributions, self.field_col_b_pac_contributions, self.field_col_b_candidate_contributions, self.field_col_b_total_contributions, self.field_col_b_transfers_from_authorized, self.field_col_b_candidate_loans, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_offset_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_authorized, self.field_col_b_candidate_loan_repayments, None, self.field_col_b_total_loan_repayments, self.field_col_b_refunds_to_individuals, None, None, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_treasurer_name, self.field_date_signed, self.field_candidate_id_number, self.field_candidate_name, self.field_report_type, self.field_col_b_gross_receipts_authorized_primary, self.field_col_b_aggregate_personal_funds_primary, self.field_col_b_gross_receipts_minus_personal_funds_primary, self.field_col_b_gross_receipts_authorized_general, self.field_col_b_aggregate_personal_funds_general, self.field_col_b_gross_receipts_minus_personal_funds_general],
              '^3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_election_state, self.field_election_district, self.field_report_code, self.field_election_code, self.field_election_date, self.field_state_of_election, self.field_primary_election, self.field_general_election, self.field_special_election, self.field_runoff_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_total_contributions_no_loans, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_operating_expenditures, self.field_col_a_total_offset_to_operating_expenditures, self.field_col_a_net_operating_expenditures, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individual_contributions_itemized, self.field_col_a_individual_contributions_unitemized, self.field_col_a_total_individual_contributions, self.field_col_a_political_party_contributions, self.field_col_a_pac_contributions, self.field_col_a_candidate_contributions, self.field_col_a_total_contributions, self.field_col_a_transfers_from_authorized, self.field_col_a_candidate_loans, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_offset_to_operating_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_authorized, self.field_col_a_candidate_loan_repayments, self.field_col_a_other_loan_repayments, self.field_col_a_total_loan_repayments, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_cash_beginning_reporting_period, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_receipts_period, self.field_col_a_cash_on_hand_close, self.field_col_b_total_contributions_no_loans, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_operating_expenditures, self.field_col_b_total_offset_to_operating_expenditures, self.field_col_b_net_operating_expenditures, self.field_col_b_individual_contributions_itemized, self.field_col_b_individual_contributions_unitemized, self.field_col_b_total_individual_contributions, self.field_col_b_political_party_contributions, self.field_col_b_pac_contributions, self.field_col_b_candidate_contributions, self.field_col_b_total_contributions, self.field_col_b_transfers_from_authorized, self.field_col_b_candidate_loans, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_offset_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_authorized, self.field_col_b_candidate_loan_repayments, self.field_col_b_other_loan_repayments, self.field_col_b_total_loan_repayments, self.field_col_b_refunds_to_individuals, self.field_col_b_refunds_to_party_committees, self.field_col_b_refunds_to_other_committees, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_treasurer_name, self.field_date_signed],
            },
            "^f3l[a|n]" : {
              '^8.0|7.0|6.4' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_election_state, self.field_election_district, self.field_report_code, self.field_election_date, None, self.field_semi_annual_period, self.field_coverage_from_date, self.field_coverage_through_date, self.field_semi_annual_period_jan_june, self.field_semi_annual_period_jul_dec, self.field_quarterly_monthly_bundled_contributions, self.field_semi_annual_bundled_contributions, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed],
            },
            "(^f3p$)|(^f3p[^s|3])" : {
              '^7.0|8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_activity_primary, self.field_activity_general, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_expenditures_subject_to_limits, self.field_col_a_net_contributions, self.field_col_a_net_operating_expenditures, self.field_col_a_federal_funds, self.field_col_a_individuals_itemized, self.field_col_a_individuals_unitemized, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees_receipts, self.field_col_a_other_political_committees_pacs, self.field_col_a_the_candidate, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_received_from_or_guaranteed_by_cand, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_operating, self.field_col_a_fundraising, self.field_col_a_legal_and_accounting, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_other_authorized_committees, self.field_col_a_fundraising_disbursements, self.field_col_a_exempt_legal_accounting_disbursement, self.field_col_a_made_or_guaranteed_by_candidate, self.field_col_a_other_repayments, self.field_col_a_total_loan_repayments_made, self.field_col_a_individuals, self.field_col_a_political_party_committees_refunds, self.field_col_a_other_political_committees, self.field_col_a_total_contributions_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_items_on_hand_to_be_liquidated, self.field_col_a_alabama, self.field_col_a_alaska, self.field_col_a_arizona, self.field_col_a_arkansas, self.field_col_a_california, self.field_col_a_colorado, self.field_col_a_connecticut, self.field_col_a_delaware, self.field_col_a_dist_of_columbia, self.field_col_a_florida, self.field_col_a_georgia, self.field_col_a_hawaii, self.field_col_a_idaho, self.field_col_a_illinois, self.field_col_a_indiana, self.field_col_a_iowa, self.field_col_a_kansas, self.field_col_a_kentucky, self.field_col_a_louisiana, self.field_col_a_maine, self.field_col_a_maryland, self.field_col_a_massachusetts, self.field_col_a_michigan, self.field_col_a_minnesota, self.field_col_a_mississippi, self.field_col_a_missouri, self.field_col_a_montana, self.field_col_a_nebraska, self.field_col_a_nevada, self.field_col_a_new_hampshire, self.field_col_a_new_jersey, self.field_col_a_new_mexico, self.field_col_a_new_york, self.field_col_a_north_carolina, self.field_col_a_north_dakota, self.field_col_a_ohio, self.field_col_a_oklahoma, self.field_col_a_oregon, self.field_col_a_pennsylvania, self.field_col_a_rhode_island, self.field_col_a_south_carolina, self.field_col_a_south_dakota, self.field_col_a_tennessee, self.field_col_a_texas, self.field_col_a_utah, self.field_col_a_vermont, self.field_col_a_virginia, self.field_col_a_washington, self.field_col_a_west_virginia, self.field_col_a_wisconsin, self.field_col_a_wyoming, self.field_col_a_puerto_rico, self.field_col_a_guam, self.field_col_a_virgin_islands, self.field_col_a_totals, self.field_col_b_federal_funds, self.field_col_b_individuals_itemized, self.field_col_b_individuals_unitemized, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees_receipts, self.field_col_b_other_political_committees_pacs, self.field_col_b_the_candidate, self.field_col_b_total_contributions_other_than_loans, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_received_from_or_guaranteed_by_cand, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_operating, self.field_col_b_fundraising, self.field_col_b_legal_and_accounting, self.field_col_b_total_offsets_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_other_authorized_committees, self.field_col_b_fundraising_disbursements, self.field_col_b_exempt_legal_accounting_disbursement, self.field_col_b_made_or_guaranteed_by_the_candidate, self.field_col_b_other_repayments, self.field_col_b_total_loan_repayments_made, self.field_col_b_individuals, self.field_col_b_political_party_committees_refunds, self.field_col_b_other_political_committees, self.field_col_b_total_contributions_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_alabama, self.field_col_b_alaska, self.field_col_b_arizona, self.field_col_b_arkansas, self.field_col_b_california, self.field_col_b_colorado, self.field_col_b_connecticut, self.field_col_b_delaware, self.field_col_b_dist_of_columbia, self.field_col_b_florida, self.field_col_b_georgia, self.field_col_b_hawaii, self.field_col_b_idaho, self.field_col_b_illinois, self.field_col_b_indiana, self.field_col_b_iowa, self.field_col_b_kansas, self.field_col_b_kentucky, self.field_col_b_louisiana, self.field_col_b_maine, self.field_col_b_maryland, self.field_col_b_massachusetts, self.field_col_b_michigan, self.field_col_b_minnesota, self.field_col_b_mississippi, self.field_col_b_missouri, self.field_col_b_montana, self.field_col_b_nebraska, self.field_col_b_nevada, self.field_col_b_new_hampshire, self.field_col_b_new_jersey, self.field_col_b_new_mexico, self.field_col_b_new_york, self.field_col_b_north_carolina, self.field_col_b_north_dakota, self.field_col_b_ohio, self.field_col_b_oklahoma, self.field_col_b_oregon, self.field_col_b_pennsylvania, self.field_col_b_rhode_island, self.field_col_b_south_carolina, self.field_col_b_south_dakota, self.field_col_b_tennessee, self.field_col_b_texas, self.field_col_b_utah, self.field_col_b_vermont, self.field_col_b_virginia, self.field_col_b_washington, self.field_col_b_west_virginia, self.field_col_b_wisconsin, self.field_col_b_wyoming, self.field_col_b_puerto_rico, self.field_col_b_guam, self.field_col_b_virgin_islands, self.field_col_b_totals],
              '^6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_activity_primary, self.field_activity_general, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_expenditures_subject_to_limits, self.field_col_a_net_contributions, self.field_col_a_net_operating_expenditures, self.field_col_a_federal_funds, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees_receipts, self.field_col_a_other_political_committees_pacs, self.field_col_a_the_candidate, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_received_from_or_guaranteed_by_cand, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_operating, self.field_col_a_fundraising, self.field_col_a_legal_and_accounting, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_other_authorized_committees, self.field_col_a_fundraising_disbursements, self.field_col_a_exempt_legal_accounting_disbursement, self.field_col_a_made_or_guaranteed_by_candidate, self.field_col_a_other_repayments, self.field_col_a_total_loan_repayments_made, self.field_col_a_individuals, self.field_col_a_political_party_committees_refunds, self.field_col_a_other_political_committees, self.field_col_a_total_contributions_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_items_on_hand_to_be_liquidated, self.field_col_a_alabama, self.field_col_a_alaska, self.field_col_a_arizona, self.field_col_a_arkansas, self.field_col_a_california, self.field_col_a_colorado, self.field_col_a_connecticut, self.field_col_a_delaware, self.field_col_a_dist_of_columbia, self.field_col_a_florida, self.field_col_a_georgia, self.field_col_a_hawaii, self.field_col_a_idaho, self.field_col_a_illinois, self.field_col_a_indiana, self.field_col_a_iowa, self.field_col_a_kansas, self.field_col_a_kentucky, self.field_col_a_louisiana, self.field_col_a_maine, self.field_col_a_maryland, self.field_col_a_massachusetts, self.field_col_a_michigan, self.field_col_a_minnesota, self.field_col_a_mississippi, self.field_col_a_missouri, self.field_col_a_montana, self.field_col_a_nebraska, self.field_col_a_nevada, self.field_col_a_new_hampshire, self.field_col_a_new_jersey, self.field_col_a_new_mexico, self.field_col_a_new_york, self.field_col_a_north_carolina, self.field_col_a_north_dakota, self.field_col_a_ohio, self.field_col_a_oklahoma, self.field_col_a_oregon, self.field_col_a_pennsylvania, self.field_col_a_rhode_island, self.field_col_a_south_carolina, self.field_col_a_south_dakota, self.field_col_a_tennessee, self.field_col_a_texas, self.field_col_a_utah, self.field_col_a_vermont, self.field_col_a_virginia, self.field_col_a_washington, self.field_col_a_west_virginia, self.field_col_a_wisconsin, self.field_col_a_wyoming, self.field_col_a_puerto_rico, self.field_col_a_guam, self.field_col_a_virgin_islands, self.field_col_a_totals, self.field_col_b_federal_funds, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees_receipts, self.field_col_b_other_political_committees_pacs, self.field_col_b_the_candidate, self.field_col_b_total_contributions_other_than_loans, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_received_from_or_guaranteed_by_cand, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_operating, self.field_col_b_fundraising, self.field_col_b_legal_and_accounting, self.field_col_b_total_offsets_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_other_authorized_committees, self.field_col_b_fundraising_disbursements, self.field_col_b_exempt_legal_accounting_disbursement, self.field_col_b_made_or_guaranteed_by_the_candidate, self.field_col_b_other_repayments, self.field_col_b_total_loan_repayments_made, self.field_col_b_individuals, self.field_col_b_political_party_committees_refunds, self.field_col_b_other_political_committees, self.field_col_b_total_contributions_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_alabama, self.field_col_b_alaska, self.field_col_b_arizona, self.field_col_b_arkansas, self.field_col_b_california, self.field_col_b_colorado, self.field_col_b_connecticut, self.field_col_b_delaware, self.field_col_b_dist_of_columbia, self.field_col_b_florida, self.field_col_b_georgia, self.field_col_b_hawaii, self.field_col_b_idaho, self.field_col_b_illinois, self.field_col_b_indiana, self.field_col_b_iowa, self.field_col_b_kansas, self.field_col_b_kentucky, self.field_col_b_louisiana, self.field_col_b_maine, self.field_col_b_maryland, self.field_col_b_massachusetts, self.field_col_b_michigan, self.field_col_b_minnesota, self.field_col_b_mississippi, self.field_col_b_missouri, self.field_col_b_montana, self.field_col_b_nebraska, self.field_col_b_nevada, self.field_col_b_new_hampshire, self.field_col_b_new_jersey, self.field_col_b_new_mexico, self.field_col_b_new_york, self.field_col_b_north_carolina, self.field_col_b_north_dakota, self.field_col_b_ohio, self.field_col_b_oklahoma, self.field_col_b_oregon, self.field_col_b_pennsylvania, self.field_col_b_rhode_island, self.field_col_b_south_carolina, self.field_col_b_south_dakota, self.field_col_b_tennessee, self.field_col_b_texas, self.field_col_b_utah, self.field_col_b_vermont, self.field_col_b_virginia, self.field_col_b_washington, self.field_col_b_west_virginia, self.field_col_b_wisconsin, self.field_col_b_wyoming, self.field_col_b_puerto_rico, self.field_col_b_guam, self.field_col_b_virgin_islands, self.field_col_b_totals],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_activity_primary, self.field_activity_general, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_expenditures_subject_to_limits, self.field_col_a_net_contributions, self.field_col_a_net_operating_expenditures, self.field_col_a_federal_funds, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees_receipts, self.field_col_a_other_political_committees_pacs, self.field_col_a_the_candidate, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_received_from_or_guaranteed_by_cand, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_operating, self.field_col_a_fundraising, self.field_col_a_legal_and_accounting, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_other_authorized_committees, self.field_col_a_fundraising_disbursements, self.field_col_a_exempt_legal_accounting_disbursement, self.field_col_a_made_or_guaranteed_by_candidate, self.field_col_a_other_repayments, self.field_col_a_total_loan_repayments_made, self.field_col_a_individuals, self.field_col_a_political_party_committees_refunds, self.field_col_a_other_political_committees, self.field_col_a_total_contributions_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_items_on_hand_to_be_liquidated, self.field_col_a_alabama, self.field_col_a_alaska, self.field_col_a_arizona, self.field_col_a_arkansas, self.field_col_a_california, self.field_col_a_colorado, self.field_col_a_connecticut, self.field_col_a_delaware, self.field_col_a_dist_of_columbia, self.field_col_a_florida, self.field_col_a_georgia, self.field_col_a_hawaii, self.field_col_a_idaho, self.field_col_a_illinois, self.field_col_a_indiana, self.field_col_a_iowa, self.field_col_a_kansas, self.field_col_a_kentucky, self.field_col_a_louisiana, self.field_col_a_maine, self.field_col_a_maryland, self.field_col_a_massachusetts, self.field_col_a_michigan, self.field_col_a_minnesota, self.field_col_a_mississippi, self.field_col_a_missouri, self.field_col_a_montana, self.field_col_a_nebraska, self.field_col_a_nevada, self.field_col_a_new_hampshire, self.field_col_a_new_jersey, self.field_col_a_new_mexico, self.field_col_a_new_york, self.field_col_a_north_carolina, self.field_col_a_north_dakota, self.field_col_a_ohio, self.field_col_a_oklahoma, self.field_col_a_oregon, self.field_col_a_pennsylvania, self.field_col_a_rhode_island, self.field_col_a_south_carolina, self.field_col_a_south_dakota, self.field_col_a_tennessee, self.field_col_a_texas, self.field_col_a_utah, self.field_col_a_vermont, self.field_col_a_virginia, self.field_col_a_washington, self.field_col_a_west_virginia, self.field_col_a_wisconsin, self.field_col_a_wyoming, self.field_col_a_puerto_rico, self.field_col_a_guam, self.field_col_a_virgin_islands, self.field_col_a_totals, self.field_col_b_federal_funds, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees_receipts, self.field_col_b_other_political_committees_pacs, self.field_col_b_the_candidate, self.field_col_b_total_contributions_other_than_loans, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_received_from_or_guaranteed_by_cand, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_operating, self.field_col_b_fundraising, self.field_col_b_legal_and_accounting, self.field_col_b_total_offsets_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_other_authorized_committees, self.field_col_b_fundraising_disbursements, self.field_col_b_exempt_legal_accounting_disbursement, self.field_col_b_made_or_guaranteed_by_the_candidate, self.field_col_b_other_repayments, self.field_col_b_total_loan_repayments_made, self.field_col_b_individuals, self.field_col_b_political_party_committees_refunds, self.field_col_b_other_political_committees, self.field_col_b_total_contributions_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_alabama, self.field_col_b_alaska, self.field_col_b_arizona, self.field_col_b_arkansas, self.field_col_b_california, self.field_col_b_colorado, self.field_col_b_connecticut, self.field_col_b_delaware, self.field_col_b_dist_of_columbia, self.field_col_b_florida, self.field_col_b_georgia, self.field_col_b_hawaii, self.field_col_b_idaho, self.field_col_b_illinois, self.field_col_b_indiana, self.field_col_b_iowa, self.field_col_b_kansas, self.field_col_b_kentucky, self.field_col_b_louisiana, self.field_col_b_maine, self.field_col_b_maryland, self.field_col_b_massachusetts, self.field_col_b_michigan, self.field_col_b_minnesota, self.field_col_b_mississippi, self.field_col_b_missouri, self.field_col_b_montana, self.field_col_b_nebraska, self.field_col_b_nevada, self.field_col_b_new_hampshire, self.field_col_b_new_jersey, self.field_col_b_new_mexico, self.field_col_b_new_york, self.field_col_b_north_carolina, self.field_col_b_north_dakota, self.field_col_b_ohio, self.field_col_b_oklahoma, self.field_col_b_oregon, self.field_col_b_pennsylvania, self.field_col_b_rhode_island, self.field_col_b_south_carolina, self.field_col_b_south_dakota, self.field_col_b_tennessee, self.field_col_b_texas, self.field_col_b_utah, self.field_col_b_vermont, self.field_col_b_virginia, self.field_col_b_washington, self.field_col_b_west_virginia, self.field_col_b_wisconsin, self.field_col_b_wyoming, self.field_col_b_puerto_rico, self.field_col_b_guam, self.field_col_b_virgin_islands, self.field_col_b_totals, self.field_treasurer_name, self.field_date_signed],
              '^5.1|5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_activity_primary, self.field_activity_general, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_expenditures_subject_to_limits, self.field_col_a_net_contributions, self.field_col_a_net_operating_expenditures, self.field_col_a_federal_funds, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees_receipts, self.field_col_a_other_political_committees_pacs, self.field_col_a_the_candidate, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_received_from_or_guaranteed_by_cand, self.field_col_a_other_loans, self.field_col_a_total_loans, self.field_col_a_operating, self.field_col_a_fundraising, self.field_col_a_legal_and_accounting, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_operating_expenditures, self.field_col_a_transfers_to_other_authorized_committees, self.field_col_a_fundraising_disbursements, self.field_col_a_exempt_legal_accounting_disbursement, self.field_col_a_made_or_guaranteed_by_candidate, self.field_col_a_other_repayments, self.field_col_a_total_loan_repayments_made, self.field_col_a_individuals, self.field_col_a_political_party_committees_refunds, self.field_col_a_other_political_committees, self.field_col_a_total_contributions_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_items_on_hand_to_be_liquidated, self.field_col_a_alabama, self.field_col_a_alaska, self.field_col_a_arizona, self.field_col_a_arkansas, self.field_col_a_california, self.field_col_a_colorado, self.field_col_a_connecticut, self.field_col_a_delaware, self.field_col_a_dist_of_columbia, self.field_col_a_florida, self.field_col_a_georgia, self.field_col_a_hawaii, self.field_col_a_idaho, self.field_col_a_illinois, self.field_col_a_indiana, self.field_col_a_iowa, self.field_col_a_kansas, self.field_col_a_kentucky, self.field_col_a_louisiana, self.field_col_a_maine, self.field_col_a_maryland, self.field_col_a_massachusetts, self.field_col_a_michigan, self.field_col_a_minnesota, self.field_col_a_mississippi, self.field_col_a_missouri, self.field_col_a_montana, self.field_col_a_nebraska, self.field_col_a_nevada, self.field_col_a_new_hampshire, self.field_col_a_new_jersey, self.field_col_a_new_mexico, self.field_col_a_new_york, self.field_col_a_north_carolina, self.field_col_a_north_dakota, self.field_col_a_ohio, self.field_col_a_oklahoma, self.field_col_a_oregon, self.field_col_a_pennsylvania, self.field_col_a_rhode_island, self.field_col_a_south_carolina, self.field_col_a_south_dakota, self.field_col_a_tennessee, self.field_col_a_texas, self.field_col_a_utah, self.field_col_a_vermont, self.field_col_a_virginia, self.field_col_a_washington, self.field_col_a_west_virginia, self.field_col_a_wisconsin, self.field_col_a_wyoming, self.field_col_a_puerto_rico, self.field_col_a_guam, self.field_col_a_virgin_islands, self.field_col_a_totals, self.field_col_b_federal_funds, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees_receipts, self.field_col_b_other_political_committees_pacs, self.field_col_b_the_candidate, self.field_col_b_total_contributions_other_than_loans, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_received_from_or_guaranteed_by_cand, self.field_col_b_other_loans, self.field_col_b_total_loans, self.field_col_b_operating, self.field_col_b_fundraising, self.field_col_b_legal_and_accounting, self.field_col_b_total_offsets_to_operating_expenditures, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_operating_expenditures, self.field_col_b_transfers_to_other_authorized_committees, self.field_col_b_fundraising_disbursements, self.field_col_b_exempt_legal_accounting_disbursement, self.field_col_b_made_or_guaranteed_by_the_candidate, self.field_col_b_other_repayments, self.field_col_b_total_loan_repayments_made, self.field_col_b_individuals, self.field_col_b_political_party_committees_refunds, self.field_col_b_other_political_committees, self.field_col_b_total_contributions_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_alabama, self.field_col_b_alaska, self.field_col_b_arizona, self.field_col_b_arkansas, self.field_col_b_california, self.field_col_b_colorado, self.field_col_b_connecticut, self.field_col_b_delaware, self.field_col_b_dist_of_columbia, self.field_col_b_florida, self.field_col_b_georgia, self.field_col_b_hawaii, self.field_col_b_idaho, self.field_col_b_illinois, self.field_col_b_indiana, self.field_col_b_iowa, self.field_col_b_kansas, self.field_col_b_kentucky, self.field_col_b_louisiana, self.field_col_b_maine, self.field_col_b_maryland, self.field_col_b_massachusetts, self.field_col_b_michigan, self.field_col_b_minnesota, self.field_col_b_mississippi, self.field_col_b_missouri, self.field_col_b_montana, self.field_col_b_nebraska, self.field_col_b_nevada, self.field_col_b_new_hampshire, self.field_col_b_new_jersey, self.field_col_b_new_mexico, self.field_col_b_new_york, self.field_col_b_north_carolina, self.field_col_b_north_dakota, self.field_col_b_ohio, self.field_col_b_oklahoma, self.field_col_b_oregon, self.field_col_b_pennsylvania, self.field_col_b_rhode_island, self.field_col_b_south_carolina, self.field_col_b_south_dakota, self.field_col_b_tennessee, self.field_col_b_texas, self.field_col_b_utah, self.field_col_b_vermont, self.field_col_b_virginia, self.field_col_b_washington, self.field_col_b_west_virginia, self.field_col_b_wisconsin, self.field_col_b_wyoming, self.field_col_b_puerto_rico, self.field_col_b_guam, self.field_col_b_virgin_islands, self.field_col_b_totals, self.field_treasurer_name, self.field_date_signed],
            },
            "^f3p31" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_item_description, self.field_item_contribution_aquired_date, self.field_item_fair_market_value, self.field_contributor_employer, self.field_contributor_occupation, self.field_memo_code, self.field_memo_text_description],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_contributor_employer, self.field_contributor_occupation, self.field_item_contribution_aquired_date, self.field_item_fair_market_value, self.field_transaction_code, self.field_transaction_description, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id_number],
              '^5.2|5.1|5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_contributor_employer, self.field_contributor_occupation, self.field_item_contribution_aquired_date, self.field_item_fair_market_value, self.field_transaction_code, self.field_transaction_description, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id_number],
            },
            "^f3ps" : {
              '^8.0|7.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_date_general_election, self.field_date_day_after_general_election, self.field_net_contributions, self.field_net_expenditures, self.field_federal_funds, self.field_a_i_individuals_itemized, self.field_a_ii_individuals_unitemized, self.field_a_iii_individual_contribution_total, self.field_b_political_party_committees, self.field_c_other_political_committees_pacs, self.field_d_the_candidate, self.field_e_total_contributions_other_than_loans, self.field_transfers_from_aff_other_party_committees, self.field_a_received_from_or_guaranteed_by_candidate, self.field_b_other_loans, self.field_c_total_loans, self.field_a_operating, self.field_b_fundraising, self.field_c_legal_and_accounting, self.field_d_total_offsets_to_operating_expenditures, self.field_other_receipts, self.field_total_receipts, self.field_operating_expenditures, self.field_transfers_to_other_authorized_committees, self.field_fundraising_disbursements, self.field_exempt_legal_and_accounting_disbursements, self.field_a_made_or_guaranteed_by_the_candidate, self.field_b_other_repayments, self.field_c_total_loan_repayments_made, self.field_a_individuals, self.field_b_political_party_committees, self.field_c_other_political_committees, self.field_d_total_contributions_refunds, self.field_other_disbursements, self.field_total_disbursements, self.field_alabama, self.field_alaska, self.field_arizona, self.field_arkansas, self.field_california, self.field_colorado, self.field_connecticut, self.field_delaware, self.field_dist_of_columbia, self.field_florida, self.field_georgia, self.field_hawaii, self.field_idaho, self.field_illinois, self.field_indiana, self.field_iowa, self.field_kansas, self.field_kentucky, self.field_louisiana, self.field_maine, self.field_maryland, self.field_massachusetts, self.field_michigan, self.field_minnesota, self.field_mississippi, self.field_missouri, self.field_montana, self.field_nebraska, self.field_nevada, self.field_new_hampshire, self.field_new_jersey, self.field_new_mexico, self.field_new_york, self.field_north_carolina, self.field_north_dakota, self.field_ohio, self.field_oklahoma, self.field_oregon, self.field_pennsylvania, self.field_rhode_island, self.field_south_carolina, self.field_south_dakota, self.field_tennessee, self.field_texas, self.field_utah, self.field_vermont, self.field_virginia, self.field_washington, self.field_west_virginia, self.field_wisconsin, self.field_wyoming, self.field_puerto_rico, self.field_guam, self.field_virgin_islands, self.field_totals],
              '^6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_date_general_election, self.field_date_day_after_general_election, self.field_net_contributions, self.field_net_expenditures, self.field_federal_funds, self.field_a_individuals, self.field_b_political_party_committees, self.field_c_other_political_committees_pacs, self.field_d_the_candidate, self.field_e_total_contributions_other_than_loans, self.field_transfers_from_aff_other_party_committees, self.field_a_received_from_or_guaranteed_by_candidate, self.field_b_other_loans, self.field_c_total_loans, self.field_a_operating, self.field_b_fundraising, self.field_c_legal_and_accounting, self.field_d_total_offsets_to_operating_expenditures, self.field_other_receipts, self.field_total_receipts, self.field_operating_expenditures, self.field_transfers_to_other_authorized_committees, self.field_fundraising_disbursements, self.field_exempt_legal_and_accounting_disbursements, self.field_a_made_or_guaranteed_by_the_candidate, self.field_b_other_repayments, self.field_c_total_loan_repayments_made, self.field_a_individuals, self.field_b_political_party_committees, self.field_c_other_political_committees, self.field_d_total_contributions_refunds, self.field_other_disbursements, self.field_total_disbursements, self.field_alabama, self.field_alaska, self.field_arizona, self.field_arkansas, self.field_california, self.field_colorado, self.field_connecticut, self.field_delaware, self.field_dist_of_columbia, self.field_florida, self.field_georgia, self.field_hawaii, self.field_idaho, self.field_illinois, self.field_indiana, self.field_iowa, self.field_kansas, self.field_kentucky, self.field_louisiana, self.field_maine, self.field_maryland, self.field_massachusetts, self.field_michigan, self.field_minnesota, self.field_mississippi, self.field_missouri, self.field_montana, self.field_nebraska, self.field_nevada, self.field_new_hampshire, self.field_new_jersey, self.field_new_mexico, self.field_new_york, self.field_north_carolina, self.field_north_dakota, self.field_ohio, self.field_oklahoma, self.field_oregon, self.field_pennsylvania, self.field_rhode_island, self.field_south_carolina, self.field_south_dakota, self.field_tennessee, self.field_texas, self.field_utah, self.field_vermont, self.field_virginia, self.field_washington, self.field_west_virginia, self.field_wisconsin, self.field_wyoming, self.field_puerto_rico, self.field_guam, self.field_virgin_islands, self.field_totals],
              '^5.3|5.2|5.1|5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_net_contributions, self.field_net_expenditures, self.field_federal_funds, self.field_a_individuals, self.field_b_political_party_committees, self.field_c_other_political_committees_pacs, self.field_d_the_candidate, self.field_e_total_contributions_other_than_loans, self.field_transfers_from_aff_other_party_committees, self.field_a_received_from_or_guaranteed_by_candidate, self.field_b_other_loans, self.field_c_total_loans, self.field_a_operating, self.field_b_fundraising, self.field_c_legal_and_accounting, self.field_d_total_offsets_to_operating_expenditures, self.field_other_receipts, self.field_total_receipts, self.field_operating_expenditures, self.field_transfers_to_other_authorized_committees, self.field_fundraising_disbursements, self.field_exempt_legal_and_accounting_disbursements, self.field_a_made_or_guaranteed_by_the_candidate, self.field_b_other_repayments, self.field_c_total_loan_repayments_made, self.field_a_individuals, self.field_b_political_party_committees, self.field_c_other_political_committees, self.field_d_total_contributions_refunds, self.field_other_disbursements, self.field_total_disbursements, self.field_alabama, self.field_alaska, self.field_arizona, self.field_arkansas, self.field_california, self.field_colorado, self.field_connecticut, self.field_delaware, self.field_dist_of_columbia, self.field_florida, self.field_georgia, self.field_hawaii, self.field_idaho, self.field_illinois, self.field_indiana, self.field_iowa, self.field_kansas, self.field_kentucky, self.field_louisiana, self.field_maine, self.field_maryland, self.field_massachusetts, self.field_michigan, self.field_minnesota, self.field_mississippi, self.field_missouri, self.field_montana, self.field_nebraska, self.field_nevada, self.field_new_hampshire, self.field_new_jersey, self.field_new_mexico, self.field_new_york, self.field_north_carolina, self.field_north_dakota, self.field_ohio, self.field_oklahoma, self.field_oregon, self.field_pennsylvania, self.field_rhode_island, self.field_south_carolina, self.field_south_dakota, self.field_tennessee, self.field_texas, self.field_utah, self.field_vermont, self.field_virginia, self.field_washington, self.field_west_virginia, self.field_wisconsin, self.field_wyoming, self.field_puerto_rico, self.field_guam, self.field_virgin_islands, self.field_totals, self.field_date_general_election, self.field_date_day_after_general_election],
            },
            "^f3s" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_date_general_election, self.field_date_day_after_general_election, self.field_a_total_contributions_no_loans, self.field_b_total_contribution_refunds, self.field_c_net_contributions, self.field_a_total_operating_expenditures, self.field_b_total_offsets_to_operating_expenditures, self.field_c_net_operating_expenditures, self.field_a_i_individuals_itemized, self.field_a_ii_individuals_unitemized, self.field_a_iii_individuals_total, self.field_b_political_party_committees, self.field_c_all_other_political_committees_pacs, self.field_d_the_candidate, self.field_e_total_contributions, self.field_transfers_from_other_auth_committees, self.field_a_loans_made_or_guarn_by_the_candidate, self.field_b_all_other_loans, self.field_c_total_loans, self.field_offsets_to_operating_expenditures, self.field_other_receipts, self.field_total_receipts, self.field_operating_expenditures, self.field_transfers_to_other_auth_committees, self.field_a_loan_repayment_by_candidate, self.field_b_loan_repayments_all_other_loans, self.field_c_total_loan_repayments, self.field_a_refund_individuals_other_than_pol_cmtes, self.field_b_refund_political_party_committees, self.field_c_refund_other_political_committees, self.field_d_total_contributions_refunds, self.field_other_disbursements, self.field_total_disbursements],
              '^5.3|5.2|5.1|5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_a_total_contributions_no_loans, self.field_b_total_contribution_refunds, self.field_c_net_contributions, self.field_a_total_operating_expenditures, self.field_b_total_offsets_to_operating_expenditures, self.field_c_net_operating_expenditures, self.field_a_i_individuals_itemized, self.field_a_ii_individuals_unitemized, self.field_a_iii_individuals_total, self.field_b_political_party_committees, self.field_c_all_other_political_committees_pacs, self.field_d_the_candidate, self.field_e_total_contributions, self.field_transfers_from_other_auth_committees, self.field_a_loans_made_or_guarn_by_the_candidate, self.field_b_all_other_loans, self.field_c_total_loans, self.field_offsets_to_operating_expenditures, self.field_other_receipts, self.field_total_receipts, self.field_operating_expenditures, self.field_transfers_to_other_auth_committees, self.field_a_loan_repayment_by_candidate, None, self.field_c_total_loan_repayments, self.field_a_refund_individuals_other_than_pol_cmtes, None, None, self.field_d_total_contributions_refunds, self.field_other_disbursements, self.field_total_disbursements, self.field_date_general_election, self.field_date_day_after_general_election],
            },
            "(^f3x$)|(^f3x[ant])" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_qualified_committee, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individuals_itemized, self.field_col_a_individuals_unitemized, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees, self.field_col_a_other_political_committees_pacs, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_total_loans, self.field_col_a_total_loan_repayments_received, self.field_col_a_offsets_to_expenditures, self.field_col_a_total_contributions_refunds, self.field_col_a_other_federal_receipts, self.field_col_a_transfers_from_nonfederal_h3, self.field_col_a_levin_funds, self.field_col_a_total_nonfederal_transfers, self.field_col_a_total_receipts, self.field_col_a_total_federal_receipts, self.field_col_a_shared_operating_expenditures_federal, self.field_col_a_shared_operating_expenditures_nonfederal, self.field_col_a_other_federal_operating_expenditures, self.field_col_a_total_operating_expenditures, self.field_col_a_transfers_to_affiliated, self.field_col_a_contributions_to_candidates, self.field_col_a_independent_expenditures, self.field_col_a_coordinated_expenditures_by_party_committees, self.field_col_a_total_loan_repayments_made, self.field_col_a_loans_made, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_federal_election_activity_federal_share, self.field_col_a_federal_election_activity_levin_share, self.field_col_a_federal_election_activity_all_federal, self.field_col_a_federal_election_activity_total, self.field_col_a_total_disbursements, self.field_col_a_total_federal_disbursements, self.field_col_a_total_contributions, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_federal_operating_expenditures, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_net_operating_expenditures, self.field_col_b_cash_on_hand_jan_1, self.field_col_b_year, self.field_col_b_total_receipts, self.field_col_b_subtotal, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_close_of_period, self.field_col_b_individuals_itemized, self.field_col_b_individuals_unitemized, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees, self.field_col_b_other_political_committees_pacs, self.field_col_b_total_contributions, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_total_loans, self.field_col_b_total_loan_repayments_received, self.field_col_b_offsets_to_expenditures, self.field_col_b_total_contributions_refunds, self.field_col_b_other_federal_receipts, self.field_col_b_transfers_from_nonfederal_h3, self.field_col_b_levin_funds, self.field_col_b_total_nonfederal_transfers, self.field_col_b_total_receipts, self.field_col_b_total_federal_receipts, self.field_col_b_shared_operating_expenditures_federal, self.field_col_b_shared_operating_expenditures_nonfederal, self.field_col_b_other_federal_operating_expenditures, self.field_col_b_total_operating_expenditures, self.field_col_b_transfers_to_affiliated, self.field_col_b_contributions_to_candidates, self.field_col_b_independent_expenditures, self.field_col_b_coordinated_expenditures_by_party_committees, self.field_col_b_total_loan_repayments_made, self.field_col_b_loans_made, self.field_col_b_refunds_to_individuals, self.field_col_b_refunds_to_party_committees, self.field_col_b_refunds_to_other_committees, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_federal_election_activity_federal_share, self.field_col_b_federal_election_activity_levin_share, self.field_col_b_federal_election_activity_all_federal, self.field_col_b_federal_election_activity_total, self.field_col_b_total_disbursements, self.field_col_b_total_federal_disbursements, self.field_col_b_total_contributions, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_federal_operating_expenditures, self.field_col_b_total_offsets_to_expenditures, self.field_col_b_net_operating_expenditures],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_qualified_committee, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_b_cash_on_hand_jan_1, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individuals_itemized, self.field_col_a_individuals_unitemized, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees, self.field_col_a_other_political_committees_pacs, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_total_loans, self.field_col_a_total_loan_repayments_received, self.field_col_a_offsets_to_expenditures, self.field_col_a_total_contributions_refunds, self.field_col_a_other_federal_receipts, self.field_col_a_transfers_from_nonfederal_h3, self.field_col_a_total_receipts, self.field_col_a_total_federal_receipts, self.field_col_a_shared_operating_expenditures_federal, self.field_col_a_shared_operating_expenditures_nonfederal, self.field_col_a_other_federal_operating_expenditures, self.field_col_a_total_operating_expenditures, self.field_col_a_transfers_to_affiliated, self.field_col_a_contributions_to_candidates, self.field_col_a_independent_expenditures, self.field_col_a_coordinated_expenditures_by_party_committees, self.field_col_a_total_loan_repayments_made, self.field_col_a_loans_made, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_total_federal_disbursements, self.field_col_a_total_contributions, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_federal_operating_expenditures, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_net_operating_expenditures, None, self.field_col_b_year, self.field_col_b_total_receipts, self.field_col_b_subtotal, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_close_of_period, self.field_col_b_individuals_itemized, self.field_col_b_individuals_unitemized, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees, self.field_col_b_other_political_committees_pacs, self.field_col_b_total_contributions, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_total_loans, self.field_col_b_total_loan_repayments_received, self.field_col_b_offsets_to_expenditures, self.field_col_b_total_contributions_refunds, self.field_col_b_other_federal_receipts, self.field_col_b_transfers_from_nonfederal_h3, self.field_col_b_total_receipts, self.field_col_b_total_federal_receipts, self.field_col_b_shared_operating_expenditures_federal, self.field_col_b_shared_operating_expenditures_nonfederal, self.field_col_b_other_federal_operating_expenditures, self.field_col_b_total_operating_expenditures, self.field_col_b_transfers_to_affiliated, self.field_col_b_contributions_to_candidates, self.field_col_b_independent_expenditures, self.field_col_b_coordinated_expenditures_by_party_committees, self.field_col_b_total_loan_repayments_made, self.field_col_b_loans_made, self.field_col_b_refunds_to_individuals, self.field_col_b_refunds_to_party_committees, self.field_col_b_refunds_to_other_committees, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_total_federal_disbursements, self.field_col_b_total_contributions, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_federal_operating_expenditures, self.field_col_b_total_offsets_to_expenditures, self.field_col_b_net_operating_expenditures, self.field_treasurer_name, self.field_date_signed, self.field_col_a_levin_funds, self.field_col_a_total_nonfederal_transfers, self.field_col_a_federal_election_activity_federal_share, self.field_col_a_federal_election_activity_levin_share, self.field_col_a_federal_election_activity_all_federal, self.field_col_a_federal_election_activity_total, self.field_col_b_levin_funds, self.field_col_b_total_nonfederal_transfers, self.field_col_b_federal_election_activity_federal_share, self.field_col_b_federal_election_activity_levin_share, self.field_col_b_federal_election_activity_all_federal, self.field_col_b_federal_election_activity_total],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_col_b_cash_on_hand_jan_1, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_qualified_committee, self.field_report_code, self.field_election_code, self.field_date_of_election, self.field_state_of_election, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_individuals_itemized, self.field_col_a_individuals_unitemized, self.field_col_a_individual_contribution_total, self.field_col_a_political_party_committees, self.field_col_a_other_political_committees_pacs, self.field_col_a_total_contributions, self.field_col_a_transfers_from_aff_other_party_cmttees, self.field_col_a_total_loans, self.field_col_a_total_loan_repayments_received, self.field_col_a_offsets_to_expenditures, self.field_col_a_total_contributions_refunds, self.field_col_a_other_federal_receipts, self.field_col_a_transfers_from_nonfederal_h3, self.field_col_a_total_receipts, self.field_col_a_total_federal_receipts, self.field_col_a_shared_operating_expenditures_federal, self.field_col_a_shared_operating_expenditures_nonfederal, self.field_col_a_other_federal_operating_expenditures, self.field_col_a_total_operating_expenditures, self.field_col_a_transfers_to_affiliated, self.field_col_a_contributions_to_candidates, self.field_col_a_independent_expenditures, self.field_col_a_coordinated_expenditures_by_party_committees, self.field_col_a_total_loan_repayments_made, self.field_col_a_loans_made, self.field_col_a_refunds_to_individuals, self.field_col_a_refunds_to_party_committees, self.field_col_a_refunds_to_other_committees, self.field_col_a_total_refunds, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_total_federal_disbursements, self.field_col_a_total_contributions, self.field_col_a_total_contributions_refunds, self.field_col_a_net_contributions, self.field_col_a_total_federal_operating_expenditures, self.field_col_a_total_offsets_to_expenditures, self.field_col_a_net_operating_expenditures, None, self.field_col_b_year, self.field_col_b_total_receipts, self.field_col_b_subtotal, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_close_of_period, self.field_col_b_individuals_itemized, self.field_col_b_individuals_unitemized, self.field_col_b_individual_contribution_total, self.field_col_b_political_party_committees, self.field_col_b_other_political_committees_pacs, self.field_col_b_total_contributions, self.field_col_b_transfers_from_aff_other_party_cmttees, self.field_col_b_total_loans, self.field_col_b_total_loan_repayments_received, self.field_col_b_offsets_to_expenditures, self.field_col_b_total_contributions_refunds, self.field_col_b_other_federal_receipts, self.field_col_b_transfers_from_nonfederal_h3, self.field_col_b_total_receipts, self.field_col_b_total_federal_receipts, self.field_col_b_shared_operating_expenditures_federal, self.field_col_b_shared_operating_expenditures_nonfederal, self.field_col_b_other_federal_operating_expenditures, self.field_col_b_total_operating_expenditures, self.field_col_b_transfers_to_affiliated, self.field_col_b_contributions_to_candidates, self.field_col_b_independent_expenditures, self.field_col_b_coordinated_expenditures_by_party_committees, self.field_col_b_total_loan_repayments_made, self.field_col_b_loans_made, self.field_col_b_refunds_to_individuals, self.field_col_b_refunds_to_party_committees, self.field_col_b_refunds_to_other_committees, self.field_col_b_total_refunds, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_total_federal_disbursements, self.field_col_b_total_contributions, self.field_col_b_total_contributions_refunds, self.field_col_b_net_contributions, self.field_col_b_total_federal_operating_expenditures, self.field_col_b_total_offsets_to_expenditures, self.field_col_b_net_operating_expenditures, self.field_treasurer_name, self.field_date_signed],
            },
            "^f4[na]" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_committee_type, self.field_committee_type_description, self.field_report_code, self.field_coverage_from_date, self.field_coverage_through_date, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_col_a_cash_on_hand_beginning_reporting_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_convention_expenditures, self.field_col_a_convention_refunds, self.field_col_a_expenditures_subject_to_limits, self.field_col_a_prior_expenditures_subject_to_limits, self.field_col_a_federal_funds, self.field_col_a_contributions_itemized, self.field_col_a_contributions_unitemized, self.field_col_a_contributions_subtotal, self.field_col_b_transfers_from_affiliated, self.field_col_a_loans_received, self.field_col_a_loan_repayments_received, self.field_col_a_loan_receipts_subtotal, self.field_col_a_convention_refunds_itemized, self.field_col_a_convention_refunds_unitemized, self.field_col_a_convention_refunds_subtotal, self.field_col_a_other_refunds_itemized, self.field_col_a_other_refunds_unitemized, self.field_col_a_other_refunds_subtotal, self.field_col_a_other_income_itemized, self.field_col_a_other_income_unitemized, self.field_col_a_other_income_subtotal, self.field_col_a_total_receipts, self.field_col_a_convention_expenses_itemized, self.field_col_a_convention_expenses_unitemized, self.field_col_a_convention_expenses_subtotal, self.field_col_a_transfers_to_affiliated, self.field_col_a_loans_made, self.field_col_a_loan_repayments_made, self.field_col_a_loan_disbursements_subtotal, self.field_col_a_other_disbursements_itemized, self.field_col_a_other_disbursements_unitemized, self.field_col_a_other_disbursements_subtotal, self.field_col_a_total_disbursements, self.field_col_b_cash_on_hand_beginning_year, self.field_col_b_beginning_year, self.field_col_b_total_receipts, self.field_col_b_subtotal, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_close_of_period, self.field_col_b_convention_expenditures, self.field_col_b_convention_refunds, self.field_col_b_expenditures_subject_to_limits, self.field_col_b_prior_expendiutres_subject_to_limits, self.field_col_b_total_expenditures_subject_to_limits, self.field_col_b_federal_funds, self.field_col_b_contributions_subtotal, self.field_col_b_transfers_from_affiliated, self.field_col_b_loan_receipts_subtotal, self.field_col_b_convention_refunds_subtotal, self.field_col_b_other_refunds_subtotal, self.field_col_b_other_income_subtotal, self.field_col_b_total_receipts, self.field_col_b_convention_expenses_subtotal, self.field_col_b_transfers_to_affiliated, self.field_col_b_loan_disbursements_subtotal, self.field_col_b_other_disbursements_subtotal, self.field_col_b_total_disbursements],
              '^5.3|5.2|5.1|5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_committee_type, self.field_committee_type_description, self.field_report_code, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_cash_on_hand_beginning_reporting_period, self.field_col_a_total_receipts, self.field_col_a_subtotal, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_close_of_period, self.field_col_a_debts_to, self.field_col_a_debts_by, self.field_col_a_convention_expenditures, self.field_col_a_convention_refunds, self.field_col_a_expenditures_subject_to_limits, self.field_col_a_prior_expenditures_subject_to_limits, self.field_col_a_total_expenditures_subject_to_limits, self.field_col_a_federal_funds, self.field_col_a_contributions_itemized, self.field_col_a_contributions_unitemized, self.field_col_a_contributions_subtotal, self.field_col_b_transfers_from_affiliated, self.field_col_a_loans_received, self.field_col_a_loan_repayments_received, self.field_col_a_loan_receipts_subtotal, self.field_col_a_convention_refunds_itemized, self.field_col_a_convention_refunds_unitemized, self.field_col_a_convention_refunds_subtotal, self.field_col_a_other_refunds_itemized, self.field_col_a_other_refunds_unitemized, self.field_col_a_other_refunds_subtotal, self.field_col_a_other_income_itemized, self.field_col_a_other_income_unitemized, self.field_col_a_other_income_subtotal, self.field_col_a_total_receipts, self.field_col_a_convention_expenses_itemized, self.field_col_a_convention_expenses_unitemized, self.field_col_a_convention_expenses_subtotal, self.field_col_a_transfers_to_affiliated, self.field_col_a_loans_made, self.field_col_a_loan_repayments_made, self.field_col_a_loan_disbursements_subtotal, self.field_col_a_other_disbursements_itemized, self.field_col_a_other_disbursements_unitemized, self.field_col_a_other_disbursements_subtotal, self.field_col_a_total_disbursements, self.field_col_b_cash_on_hand_beginning_year, self.field_col_b_beginning_year, self.field_col_b_total_receipts, self.field_col_b_subtotal, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_close_of_period, self.field_col_b_convention_expenditures, self.field_col_b_convention_refunds, self.field_col_b_expenditures_subject_to_limits, self.field_col_b_prior_expendiutres_subject_to_limits, self.field_col_b_total_expenditures_subject_to_limits, self.field_col_b_federal_funds, self.field_col_b_contributions_subtotal, self.field_col_b_transfers_from_affiliated, self.field_col_b_loan_receipts_subtotal, self.field_col_b_convention_refunds_subtotal, self.field_col_b_other_refunds_subtotal, self.field_col_b_other_income_subtotal, self.field_col_b_total_receipts, self.field_col_b_convention_expenses_subtotal, self.field_col_b_transfers_to_affiliated, self.field_col_b_loan_disbursements_subtotal, self.field_col_b_other_disbursements_subtotal, self.field_col_b_total_disbursements, self.field_treasurer_name, self.field_date_signed],
            },
            "^f5[na]" : {
              '^8.0|7.0|6.4|6.3|6.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_organization_name, self.field_individual_last_name, self.field_individual_first_name, self.field_individual_middle_name, self.field_individual_prefix, self.field_individual_suffix, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_qualified_nonprofit, self.field_individual_employer, self.field_individual_occupation, self.field_report_code, self.field_report_type, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_contribution, self.field_total_independent_expenditure, self.field_person_completing_last_name, self.field_person_completing_first_name, self.field_person_completing_middle_name, self.field_person_completing_prefix, self.field_person_completing_suffix, self.field_date_signed],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_qualified_nonprofit, self.field_individual_employer, None, self.field_report_code, None, None, None, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_contribution, self.field_total_independent_expenditure, self.field_person_completing_name, self.field_date_signed, None, None, None, self.field_report_type],
              '^5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_qualified_nonprofit, self.field_individual_employer, self.field_individual_occupation, self.field_report_code, self.field_report_pgi, self.field_election_date, self.field_election_state, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_contribution, self.field_total_independent_expenditure, self.field_person_completing_name, self.field_date_signed, self.field_date_notarized, self.field_date_notary_commission_expires, self.field_notary_name, self.field_report_type],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_qualified_nonprofit, self.field_individual_employer, self.field_individual_occupation, self.field_report_code, self.field_report_pgi, self.field_election_date, self.field_election_state, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_contribution, self.field_total_independent_expenditure, self.field_person_completing_name, self.field_date_signed, self.field_date_notarized, self.field_date_notary_commission_expires, self.field_notary_name],
            },
            "^f56" : {
              '^8.0|7.0|6.4|6.3|6.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_contributor_fec_id, self.field_contribution_date, self.field_contribution_amount, self.field_contributor_employer, self.field_contributor_occupation],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_date, self.field_contribution_amount, self.field_contributor_fec_id, self.field_candidate_id, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id],
            },
            "^f57" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_calendar_y_t_d_per_election_office, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_payee_cmtte_fec_id_number, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district],
              '^7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_calendar_y_t_d_per_election_office, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_payee_cmtte_fec_id_number, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, None, None, None, None, None, None, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number, self.field_category_code, self.field_expenditure_purpose_code, self.field_calendar_y_t_d_per_election_office, self.field_election_code, self.field_election_other_description],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_2, None, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, None, None, None, None, None, None, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_amended_code],
            },
            "(^f6$)|(^f6[an])" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_original_amendment_date, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_signer_last_name, self.field_signer_first_name, self.field_signer_middle_name, self.field_signer_prefix, self.field_signer_suffix, self.field_date_signed],
              '^7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_signer_last_name, self.field_signer_first_name, self.field_signer_middle_name, self.field_signer_prefix, self.field_signer_suffix, self.field_date_signed],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_date_signed],
            },
            "^f65" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_contributor_fec_id, self.field_contribution_date, self.field_contribution_amount, self.field_contributor_employer, self.field_contributor_occupation],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_date, self.field_contribution_amount, self.field_contributor_fec_id, self.field_candidate_id, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id],
            },
            "^f7[na]" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_organization_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_organization_type, self.field_report_code, self.field_election_date, self.field_election_state, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_costs, self.field_person_designated_last_name, self.field_person_designated_first_name, self.field_person_designated_middle_name, self.field_person_designated_prefix, self.field_person_designated_suffix, self.field_person_designated_title, self.field_date_signed],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_organization_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_organization_type, self.field_report_code, self.field_election_date, self.field_election_state, self.field_coverage_from_date, self.field_coverage_through_date, self.field_total_costs, self.field_person_designated_name, self.field_date_signed, self.field_person_designated_title],
            },
            "^f76" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_communication_type, self.field_communication_type_description, self.field_communication_class, self.field_communication_date, self.field_communication_cost, self.field_election_code, self.field_election_other_description, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_communication_type, self.field_communication_type_description, self.field_communication_class, self.field_communication_date, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_code, self.field_communication_cost, None, self.field_transaction_id],
            },
            "^f9" : {
              '^8.0|7.0|6.4|6.3|6.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_organization_name, self.field_individual_last_name, self.field_individual_first_name, self.field_individual_middle_name, self.field_individual_prefix, self.field_individual_suffix, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_individual_employer, self.field_individual_occupation, self.field_coverage_from_date, self.field_coverage_through_date, self.field_date_public_distribution, self.field_communication_title, self.field_filer_code, self.field_filer_code_description, self.field_segregated_bank_account, self.field_custodian_last_name, self.field_custodian_first_name, self.field_custodian_middle_name, self.field_custodian_prefix, self.field_custodian_suffix, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_employer, self.field_custodian_occupation, self.field_total_donations, self.field_total_disbursements, self.field_person_completing_last_name, self.field_person_completing_first_name, self.field_person_completing_middle_name, self.field_person_completing_prefix, self.field_person_completing_suffix, self.field_date_signed],
              '^6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_organization_name, self.field_individual_last_name, self.field_individual_first_name, self.field_individual_middle_name, self.field_individual_prefix, self.field_individual_suffix, self.field_change_of_address, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_individual_employer, self.field_individual_occupation, self.field_coverage_from_date, self.field_coverage_through_date, self.field_date_public_distribution, self.field_communication_title, self.field_qualified_non_profit, self.field_segregated_bank_account, self.field_custodian_last_name, self.field_custodian_first_name, self.field_custodian_middle_name, self.field_custodian_prefix, self.field_custodian_suffix, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_employer, self.field_custodian_occupation, self.field_total_donations, self.field_total_disbursements, self.field_person_completing_last_name, self.field_person_completing_first_name, self.field_person_completing_middle_name, self.field_person_completing_prefix, self.field_person_completing_suffix, self.field_date_signed],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_organization_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_change_of_address, self.field_individual_employer, self.field_individual_occupation, self.field_coverage_from_date, self.field_coverage_through_date, self.field_date_public_distribution, self.field_communication_title, self.field_qualified_non_profit, self.field_segregated_bank_account, self.field_custodian_last_name, self.field_custodian_street_1, self.field_custodian_street_2, self.field_custodian_city, self.field_custodian_state, self.field_custodian_zip_code, self.field_custodian_employer, self.field_custodian_occupation, self.field_total_donations, self.field_total_disbursements, self.field_person_completing_last_name, self.field_date_signed],
            },
            "^f91" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_controller_last_name, self.field_controller_first_name, self.field_controller_middle_name, self.field_controller_prefix, self.field_controller_suffix, self.field_controller_street_1, self.field_controller_street_2, self.field_controller_city, self.field_controller_state, self.field_controller_zip_code, self.field_controller_employer, self.field_controller_occupation],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_controller_last_name, self.field_controller_street_1, self.field_controller_street_2, self.field_controller_city, self.field_controller_state, self.field_controller_zip_code, self.field_controller_employer, self.field_controller_occupation, None, self.field_transaction_id],
              '^5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_controller_last_name, self.field_controller_street_1, self.field_controller_street_2, self.field_controller_city, self.field_controller_state, self.field_controller_zip_code, self.field_controller_employer, self.field_controller_occupation, self.field_amended_cd, self.field_transaction_id],
            },
            "^f92" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_contribution_date, self.field_contribution_amount],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, None, None, self.field_contributor_employer, self.field_contributor_occupation, None, self.field_contribution_date, self.field_contribution_amount, self.field_transaction_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
              '^5.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, None, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, None, None, self.field_contributor_employer, self.field_contributor_occupation, None, self.field_contribution_date, self.field_contribution_amount, self.field_transaction_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, None, None, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix],
              '^5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, None, None, self.field_contributor_employer, self.field_contributor_occupation, None, self.field_contribution_date, self.field_contribution_amount, self.field_transaction_type, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^f93" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_expenditure_purpose_descrip, self.field_payee_employer, self.field_payee_occupation, self.field_communication_date],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, None, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, None, None, None, self.field_communication_date, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix],
              '^5.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_organization_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_descrip, self.field_expenditure_purpose_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, None, None, None, self.field_communication_date, None, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix],
              '^5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_organization_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_payee_employer, self.field_payee_occupation, None, self.field_expenditure_date, self.field_expenditure_amount, self.field_expenditure_purpose_descrip, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^f94" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_code, self.field_election_other_description],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_election_code, self.field_election_other_description, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^f99" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_text_code, self.field_text],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_treasurer_name, self.field_date_signed, self.field_text_code, self.field_text],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_committee_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_treasurer_name, self.field_date_signed, self.field_text],
            },
            "^h1" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_presidential_only_election_year, self.field_presidential_senate_election_year, self.field_senate_only_election_year, self.field_non_presidential_non_senate_election_year, self.field_flat_minimum_federal_percentage, self.field_federal_percent, self.field_nonfederal_percent, self.field_administrative_ratio_applies, self.field_generic_voter_drive_ratio_applies, self.field_public_communications_referencing_party_ratio_applies],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, self.field_presidential_only_election_year, self.field_presidential_senate_election_year, self.field_senate_only_election_year, self.field_non_presidential_non_senate_election_year, self.field_flat_minimum_federal_percentage, self.field_federal_percent, self.field_nonfederal_percent, self.field_administrative_ratio_applies, self.field_generic_voter_drive_ratio_applies, self.field_public_communications_referencing_party_ratio_applies],
              '^5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_national_party_committee_percentage, self.field_house_senate_party_committees_minimum_federal_percentage, self.field_house_senate_party_committees_percentage_federal_candidate_support, self.field_house_senate_party_committees_percentage_nonfederal_candidate_support, self.field_house_senate_party_committees_actual_federal_candidate_support, self.field_house_senate_party_committees_actual_nonfederal_candidate_support, self.field_house_senate_party_committees_percentage_actual_federal, self.field_federal_percent, self.field_nonfederal_percent, self.field_actual_direct_candidate_support_federal, self.field_actual_direct_candidate_support_nonfederal, self.field_actual_direct_candidate_support_federal_percent, self.field_ballot_presidential, self.field_ballot_senate, self.field_ballot_house, self.field_subtotal_federal, self.field_ballot_governor, self.field_ballot_other_statewide, self.field_ballot_state_senate, self.field_ballot_state_representative, self.field_ballot_local_candidates, self.field_extra_nonfederal_point, self.field_subtotal, self.field_total_points, self.field_flat_minimum_federal_percentage, None, self.field_transaction_id, self.field_presidential_only_election_year, self.field_presidential_senate_election_year, self.field_senate_only_election_year, self.field_non_presidential_non_senate_election_year],
              '^3.0' : [ self.field_ballot_local_candidates, self.field_filer_committee_id_number, self.field_national_party_committee_percentage, self.field_house_senate_party_committees_minimum_federal_percentage, self.field_house_senate_party_committees_percentage_federal_candidate_support, self.field_house_senate_party_committees_percentage_nonfederal_candidate_support, self.field_house_senate_party_committees_actual_federal_candidate_support, self.field_house_senate_party_committees_actual_nonfederal_candidate_support, self.field_house_senate_party_committees_percentage_actual_federal, self.field_federal_percent, self.field_nonfederal_percent, self.field_actual_direct_candidate_support_federal, self.field_actual_direct_candidate_support_nonfederal, self.field_actual_direct_candidate_support_federal_percent, self.field_ballot_presidential, self.field_ballot_senate, self.field_ballot_house, self.field_subtotal_federal, self.field_ballot_governor, self.field_ballot_other_statewide, self.field_ballot_state_senate, self.field_ballot_state_representative, None, self.field_extra_nonfederal_point, self.field_subtotal, self.field_total_points, self.field_flat_minimum_federal_percentage, None, self.field_transaction_id],
            },
            "^h2" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_activity_event_name, self.field_direct_fundraising, self.field_direct_candidate_support, self.field_ratio_code, self.field_federal_percentage, self.field_nonfederal_percentage],
              '^5.3|5.2|5.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_activity_event_name, self.field_direct_fundraising, None, self.field_direct_candidate_support, self.field_ratio_code, self.field_federal_percentage, self.field_nonfederal_percentage, None, self.field_transaction_id],
              '^5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_activity_event_name, self.field_direct_fundraising, self.field_exempt_activity, self.field_direct_candidate_support, self.field_ratio_code, self.field_federal_percentage, self.field_nonfederal_percentage, None, self.field_transaction_id],
            },
            "^h3" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_account_name, self.field_event_type, self.field_event_activity_name, self.field_receipt_date, self.field_total_amount_transferred, self.field_transferred_amount],
              '^5.3|5.2|5.1|5.0|3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_account_name, self.field_event_activity_name, self.field_event_type, self.field_receipt_date, self.field_transferred_amount, self.field_total_amount_transferred, None, self.field_transaction_id],
            },
            "^h4" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_account_identifier, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_nonfederal_share, self.field_event_year_to_date, self.field_expenditure_purpose_description, self.field_category_code, self.field_administrative_voter_drive_activity, self.field_fundraising_activity, self.field_exempt_activity, self.field_generic_voter_drive_activity, self.field_direct_candidate_support_activity, self.field_public_communications_party_activity, self.field_memo_code, self.field_memo_text],
              '^7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_account_identifier, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_nonfederal_share, self.field_event_year_to_date, self.field_expenditure_purpose_code, self.field_expenditure_purpose_description, self.field_category_code, self.field_administrative_voter_drive_activity, self.field_fundraising_activity, self.field_exempt_activity, self.field_generic_voter_drive_activity, self.field_direct_candidate_support_activity, self.field_public_communications_party_activity, self.field_memo_code, self.field_memo_text],
              '^5.3|5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_description, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_nonfederal_share, None, self.field_fundraising_activity, self.field_exempt_activity, self.field_direct_candidate_support_activity, self.field_event_year_to_date, self.field_account_identifier, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_administrative_voter_drive_activity, self.field_generic_voter_drive_activity, self.field_category_code, self.field_expenditure_purpose_code, self.field_public_communications_party_activity],
              '^5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_description, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_nonfederal_share, None, self.field_fundraising_activity, self.field_exempt_activity, self.field_direct_candidate_support_activity, self.field_event_year_to_date, self.field_account_identifier, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_administrative_voter_drive_activity, self.field_generic_voter_drive_activity, self.field_category_code, self.field_expenditure_purpose_code],
              '^3.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_description, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_nonfederal_share, self.field_administrative_voter_drive_activity, self.field_fundraising_activity, self.field_exempt_activity, self.field_direct_candidate_support_activity, self.field_event_year_to_date, self.field_account_identifier, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_amended_cd, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^h5" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_account_name, self.field_receipt_date, self.field_total_amount_transferred, self.field_voter_registration_amount, self.field_voter_id_amount, self.field_gotv_amount, self.field_generic_campaign_amount],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_account_name, self.field_receipt_date, self.field_voter_registration_amount, self.field_voter_id_amount, self.field_gotv_amount, self.field_generic_campaign_amount, self.field_total_amount_transferred, None, self.field_transaction_id],
            },
            "^h6" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_account_identifier, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_levin_share, self.field_event_year_to_date, self.field_expenditure_purpose_description, self.field_category_code, self.field_voter_registration_activity, self.field_gotv_activity, self.field_voter_id_activity, self.field_generic_campaign_activity, self.field_memo_code, self.field_memo_text],
              '^7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_account_identifier, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_levin_share, self.field_event_year_to_date, self.field_expenditure_purpose_code, self.field_expenditure_purpose_description, self.field_category_code, self.field_voter_registration_activity, self.field_gotv_activity, self.field_voter_id_activity, self.field_generic_campaign_activity, self.field_memo_code, self.field_memo_text],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_category_code, self.field_expenditure_purpose_code, self.field_expenditure_purpose_description, self.field_expenditure_date, self.field_total_amount, self.field_federal_share, self.field_levin_share, self.field_voter_registration_activity, self.field_gotv_activity, self.field_voter_id_activity, self.field_generic_campaign_activity, self.field_event_year_to_date, self.field_account_identifier, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_committee_id, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text, None, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^sa" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_aggregate, self.field_contribution_purpose_descrip, self.field_contributor_employer, self.field_contributor_occupation, self.field_donor_committee_fec_id, self.field_donor_committee_name, self.field_donor_candidate_fec_id, self.field_donor_candidate_last_name, self.field_donor_candidate_first_name, self.field_donor_candidate_middle_name, self.field_donor_candidate_prefix, self.field_donor_candidate_suffix, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_code],
              '^7.0|6.4' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_aggregate, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_contributor_employer, self.field_contributor_occupation, self.field_donor_committee_fec_id, self.field_donor_committee_name, self.field_donor_candidate_fec_id, self.field_donor_candidate_last_name, self.field_donor_candidate_first_name, self.field_donor_candidate_middle_name, self.field_donor_candidate_prefix, self.field_donor_candidate_suffix, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_code],
              '^6.3|6.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_aggregate, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_increased_limit_code, self.field_contributor_employer, self.field_contributor_occupation, self.field_donor_committee_fec_id, self.field_donor_committee_name, self.field_donor_candidate_fec_id, self.field_donor_candidate_last_name, self.field_donor_candidate_first_name, self.field_donor_candidate_middle_name, self.field_donor_candidate_prefix, self.field_donor_candidate_suffix, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_code],
              '^6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_aggregate, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_increased_limit_code, self.field_contributor_employer, self.field_contributor_occupation, self.field_donor_committee_fec_id, self.field_donor_candidate_fec_id, self.field_donor_candidate_last_name, self.field_donor_candidate_first_name, self.field_donor_candidate_middle_name, self.field_donor_candidate_prefix, self.field_donor_candidate_suffix, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_code],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_aggregate, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_donor_committee_fec_id, self.field_donor_candidate_fec_id, self.field_donor_candidate_name, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_code, self.field_increased_limit_code, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix],
              '^5.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_aggregate, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_donor_committee_fec_id, self.field_donor_candidate_fec_id, self.field_donor_candidate_name, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_code, self.field_increased_limit_code, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix],
              '^5.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_aggregate, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_donor_committee_fec_id, self.field_donor_candidate_fec_id, self.field_donor_candidate_name, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_code, self.field_increased_limit_code, self.field_contributor_organization_name, self.field_contributor_last_name, self.field_contributor_first_name, self.field_contributor_middle_name, self.field_contributor_prefix, self.field_contributor_suffix],
              '^5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_aggregate, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_donor_committee_fec_id, self.field_donor_candidate_fec_id, self.field_donor_candidate_name, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_code, self.field_increased_limit_code],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_contributor_name, self.field_contributor_street_1, self.field_contributor_street_2, self.field_contributor_city, self.field_contributor_state, self.field_contributor_zip_code, self.field_election_code, self.field_election_other_description, self.field_contributor_employer, self.field_contributor_occupation, self.field_contribution_aggregate, self.field_contribution_date, self.field_contribution_amount, self.field_contribution_purpose_code, self.field_contribution_purpose_descrip, self.field_donor_committee_fec_id, self.field_donor_candidate_fec_id, self.field_donor_candidate_name, self.field_donor_candidate_office, self.field_donor_candidate_state, self.field_donor_candidate_district, self.field_conduit_name, self.field_conduit_street1, self.field_conduit_street2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_code],
            },
            "^sb" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_semi_annual_refunded_bundled_amt, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_beneficiary_committee_fec_id, self.field_beneficiary_committee_name, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_last_name, self.field_beneficiary_candidate_first_name, self.field_beneficiary_candidate_middle_name, self.field_beneficiary_candidate_prefix, self.field_beneficiary_candidate_suffix, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account],
              '^7.0|6.4' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_semi_annual_refunded_bundled_amt, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_beneficiary_committee_fec_id, self.field_beneficiary_committee_name, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_last_name, self.field_beneficiary_candidate_first_name, self.field_beneficiary_candidate_middle_name, self.field_beneficiary_candidate_prefix, self.field_beneficiary_candidate_suffix, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account],
              '^6.3|6.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_refund_or_disposal_of_excess, self.field_communication_date, self.field_beneficiary_committee_fec_id, self.field_beneficiary_committee_name, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_last_name, self.field_beneficiary_candidate_first_name, self.field_beneficiary_candidate_middle_name, self.field_beneficiary_candidate_prefix, self.field_beneficiary_candidate_suffix, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account],
              '^6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_refund_or_disposal_of_excess, self.field_communication_date, self.field_beneficiary_committee_fec_id, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_last_name, self.field_beneficiary_candidate_first_name, self.field_beneficiary_candidate_middle_name, self.field_beneficiary_candidate_prefix, self.field_beneficiary_candidate_suffix, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_beneficiary_committee_fec_id, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_name, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account, self.field_refund_or_disposal_of_excess, self.field_category_code, self.field_communication_date, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix],
              '^5.2|5.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_beneficiary_committee_fec_id, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_name, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account, self.field_refund_or_disposal_of_excess, self.field_category_code, self.field_communication_date, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix],
              '^5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_beneficiary_committee_fec_id, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_name, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account, self.field_refund_or_disposal_of_excess, self.field_category_code, self.field_communication_date],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_beneficiary_committee_fec_id, self.field_beneficiary_candidate_fec_id, self.field_beneficiary_candidate_name, self.field_beneficiary_candidate_office, self.field_beneficiary_candidate_state, self.field_beneficiary_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_memo_code, self.field_memo_text_description, None, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_reference_to_si_or_sl_system_code_that_identifies_the_account],
            },
            "^sc[^1-2]" : {
              '^8.0|7.0|6.4|6.3|6.2' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_receipt_line_number, self.field_entity_type, self.field_lender_organization_name, self.field_lender_last_name, self.field_lender_first_name, self.field_lender_middle_name, self.field_lender_prefix, self.field_lender_suffix, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_election_code, self.field_election_other_description, self.field_loan_amount_original, self.field_loan_payment_to_date, self.field_loan_balance, self.field_loan_incurred_date_terms, self.field_loan_due_date_terms, self.field_loan_interest_rate_terms, self.field_secured, self.field_personal_funds, self.field_lender_committee_id_number, self.field_lender_candidate_id_number, self.field_lender_candidate_last_name, self.field_lender_candidate_first_name, self.field_lender_candidate_middle_nm, self.field_lender_candidate_prefix, self.field_lender_candidate_suffix, self.field_lender_candidate_office, self.field_lender_candidate_state, self.field_lender_candidate_district, self.field_memo_code, self.field_memo_text_description],
              '^6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_receipt_line_number, self.field_entity_type, self.field_lender_organization_name, self.field_lender_last_name, self.field_lender_first_name, self.field_lender_middle_name, self.field_lender_prefix, self.field_lender_suffix, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_election_code, self.field_election_other_description, self.field_loan_amount_original, self.field_loan_payment_to_date, self.field_loan_balance, self.field_loan_incurred_date_terms, self.field_loan_due_date_terms, self.field_loan_interest_rate_terms, self.field_secured, self.field_lender_committee_id_number, self.field_lender_candidate_id_number, self.field_lender_candidate_last_name, self.field_lender_candidate_first_name, self.field_lender_candidate_middle_nm, self.field_lender_candidate_prefix, self.field_lender_candidate_suffix, self.field_lender_candidate_office, self.field_lender_candidate_state, self.field_lender_candidate_district],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_lender_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_election_code, self.field_election_other_description, self.field_loan_amount_original, self.field_loan_payment_to_date, self.field_loan_balance, self.field_loan_incurred_date_terms, self.field_loan_due_date_terms, self.field_loan_interest_rate_terms, self.field_secured, self.field_lender_committee_id_number, self.field_lender_candidate_id_number, self.field_lender_candidate_name, self.field_lender_candidate_office, self.field_lender_candidate_state, self.field_lender_candidate_district, None, self.field_transaction_id_number, self.field_receipt_line_number],
              '^5.2|5.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_lender_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_election_code, self.field_election_other_description, self.field_loan_amount_original, self.field_loan_payment_to_date, self.field_loan_balance, self.field_loan_incurred_date_terms, self.field_loan_due_date_terms, self.field_loan_interest_rate_terms, self.field_secured, self.field_lender_committee_id_number, self.field_lender_candidate_id_number, self.field_lender_candidate_name, self.field_lender_candidate_office, self.field_lender_candidate_state, self.field_lender_candidate_district, None, self.field_transaction_id_number, self.field_receipt_line_number],
              '^5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_lender_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_election_code, self.field_election_other_description, self.field_loan_amount_original, self.field_loan_payment_to_date, self.field_loan_balance, self.field_loan_incurred_date_terms, self.field_loan_due_date_terms, self.field_loan_interest_rate_terms, self.field_secured, self.field_lender_committee_id_number, self.field_lender_candidate_id_number, self.field_lender_candidate_name, self.field_lender_candidate_office, self.field_lender_candidate_state, self.field_lender_candidate_district, None, self.field_transaction_id_number],
            },
            "^sc1" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_lender_organization_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_loan_amount, self.field_loan_interest_rate, self.field_loan_incurred_date, self.field_loan_due_date, self.field_loan_restructured, self.field_loan_inccured_date_original, self.field_credit_amount_this_draw, self.field_total_balance, self.field_others_liable, self.field_collateral, self.field_description, self.field_collateral_value_amount, self.field_perfected_interest, self.field_future_income, self.field_description, self.field_estimated_value, self.field_established_date, self.field_account_location_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_deposit_acct_auth_date_presidential, self.field_f_basis_of_loan_description, self.field_treasurer_last_name, self.field_treasurer_first_name, self.field_treasurer_middle_name, self.field_treasurer_prefix, self.field_treasurer_suffix, self.field_date_signed, self.field_authorized_last_name, self.field_authorized_first_name, self.field_authorized_middle_name, self.field_authorized_prefix, self.field_authorized_suffix, self.field_authorized_title, self.field_date_signed],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_entity_type, self.field_lender_organization_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_loan_amount, self.field_loan_interest_rate, self.field_loan_incurred_date, self.field_loan_due_date, self.field_loan_restructured, self.field_loan_inccured_date_original, self.field_credit_amount_this_draw, self.field_total_balance, self.field_others_liable, self.field_collateral, self.field_description, self.field_collateral_value_amount, self.field_perfected_interest, self.field_future_income, self.field_description, self.field_estimated_value, self.field_established_date, self.field_account_location_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_deposit_acct_auth_date_presidential, self.field_f_basis_of_loan_description, self.field_treasurer_name, self.field_date_signed, self.field_authorized_name, self.field_authorized_title, self.field_date_signed],
              '^5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_entity_type, self.field_lender_organization_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_loan_amount, self.field_loan_interest_rate, self.field_loan_incurred_date, self.field_loan_due_date, self.field_loan_restructured, self.field_loan_inccured_date_original, self.field_credit_amount_this_draw, self.field_total_balance, self.field_others_liable, self.field_collateral, self.field_description, self.field_collateral_value_amount, self.field_perfected_interest, self.field_future_income, self.field_description, self.field_estimated_value, self.field_established_date, self.field_account_location_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_deposit_acct_auth_date_presidential, self.field_f_basis_of_loan_description, self.field_treasurer_name, self.field_date_signed, self.field_authorized_name, self.field_authorized_title, self.field_date_signed],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_entity_type, self.field_lender_organization_name, self.field_lender_street_1, self.field_lender_street_2, self.field_lender_city, self.field_lender_state, self.field_lender_zip_code, self.field_loan_amount, self.field_loan_interest_rate, self.field_loan_incurred_date, self.field_loan_due_date, self.field_loan_restructured, self.field_loan_inccured_date_original, self.field_credit_amount_this_draw, self.field_total_balance, self.field_others_liable, self.field_collateral, self.field_description, self.field_collateral_value_amount, self.field_perfected_interest, self.field_future_income, self.field_description, self.field_estimated_value, self.field_established_date, self.field_account_location_name, self.field_street_1, self.field_street_2, self.field_city, self.field_state, self.field_zip_code, self.field_deposit_acct_auth_date_presidential, self.field_f_basis_of_loan_description, self.field_treasurer_name, self.field_date_signed, self.field_authorized_name, self.field_authorized_title, self.field_date_signed],
            },
            "^sc2" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_guarantor_last_name, self.field_guarantor_first_name, self.field_guarantor_middle_name, self.field_guarantor_prefix, self.field_guarantor_suffix, self.field_guarantor_street_1, self.field_guarantor_street_2, self.field_guarantor_city, self.field_guarantor_state, self.field_guarantor_zip_code, self.field_guarantor_employer, self.field_guarantor_occupation, self.field_guaranteed_amount],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_guarantor_name, self.field_guarantor_street_1, self.field_guarantor_street_2, self.field_guarantor_city, self.field_guarantor_state, self.field_guarantor_zip_code, self.field_guarantor_employer, self.field_guarantor_occupation, self.field_guaranteed_amount],
              '^5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_guarantor_name, self.field_guarantor_street_1, self.field_guarantor_street_2, self.field_guarantor_city, self.field_guarantor_state, self.field_guarantor_zip_code, self.field_guarantor_employer, self.field_guarantor_occupation, self.field_guaranteed_amount],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_back_reference_tran_id_number, self.field_guarantor_name, self.field_guarantor_street_1, self.field_guarantor_street_2, self.field_guarantor_city, self.field_guarantor_state, self.field_guarantor_zip_code, self.field_guarantor_employer, self.field_guarantor_occupation, self.field_guaranteed_amount],
            },
            "^sd" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_entity_type, self.field_creditor_organization_name, self.field_creditor_last_name, self.field_creditor_first_name, self.field_creditor_middle_name, self.field_creditor_prefix, self.field_creditor_suffix, self.field_creditor_street_1, self.field_creditor_street_2, self.field_creditor_city, self.field_creditor_state, self.field_creditor_zip_code, self.field_purpose_of_debt_or_obligation, self.field_beginning_balance_this_period, self.field_incurred_amount_this_period, self.field_payment_amount_this_period, self.field_balance_at_close_this_period],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_creditor_name, self.field_creditor_street_1, self.field_creditor_street_2, self.field_creditor_city, self.field_creditor_state, self.field_creditor_zip_code, self.field_purpose_of_debt_or_obligation, self.field_beginning_balance_this_period, self.field_incurred_amount_this_period, self.field_payment_amount_this_period, self.field_balance_at_close_this_period, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number],
              '^5.2|5.1|5.0|3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_creditor_name, self.field_creditor_street_1, self.field_creditor_street_2, self.field_creditor_city, self.field_creditor_state, self.field_creditor_zip_code, self.field_purpose_of_debt_or_obligation, self.field_beginning_balance_this_period, self.field_incurred_amount_this_period, self.field_payment_amount_this_period, self.field_balance_at_close_this_period, self.field_fec_committee_id_number, self.field_fec_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number],
            },
            "^se" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_calendar_y_t_d_per_election_office, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_payee_cmtte_fec_id_number, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_completing_last_name, self.field_completing_first_name, self.field_completing_middle_name, self.field_completing_prefix, self.field_completing_suffix, self.field_date_signed, self.field_memo_code, self.field_memo_text_description],
              '^7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_election_code, self.field_election_other_description, self.field_expenditure_date, self.field_expenditure_amount, self.field_calendar_y_t_d_per_election_office, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_payee_cmtte_fec_id_number, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_last_name, self.field_candidate_first_name, self.field_candidate_middle_name, self.field_candidate_prefix, self.field_candidate_suffix, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_completing_last_name, self.field_completing_first_name, self.field_completing_middle_name, self.field_completing_prefix, self.field_completing_suffix, self.field_date_signed, self.field_memo_code, self.field_memo_text_description],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_payee_cmtte_fec_id_number, None, None, None, None, None, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_ind_name_as_signed, self.field_date_signed, self.field_date_notarized, self.field_date_notary_commission_expires, self.field_ind_name_notary, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text_description, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_election_code, self.field_election_other_description, self.field_category_code, self.field_expenditure_purpose_code, self.field_calendar_y_t_d_per_election_office],
              '^5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_payee_cmtte_fec_id_number, None, None, None, None, None, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_ind_name_as_signed, self.field_date_signed, self.field_date_notarized, self.field_date_notary_commission_expires, self.field_ind_name_notary, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text_description, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_election_code, self.field_election_other_description, self.field_category_code, self.field_expenditure_purpose_code, self.field_calendar_y_t_d_per_election_office],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_support_oppose_code, self.field_candidate_id_number, self.field_candidate_name, self.field_candidate_office, self.field_candidate_state, self.field_candidate_district, self.field_payee_cmtte_fec_id_number, None, None, None, None, None, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, self.field_ind_name_as_signed, self.field_date_signed, self.field_date_notarized, self.field_date_notary_commission_expires, self.field_ind_name_notary, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text_description, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^sf" : {
              '^8.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_coordinated_expenditures, self.field_designating_committee_id_number, self.field_designating_committee_name, self.field_subordinate_committee_id_number, self.field_subordinate_committee_name, self.field_subordinate_street_1, self.field_subordinate_street_2, self.field_subordinate_city, self.field_subordinate_state, self.field_subordinate_zip_code, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_date, self.field_expenditure_amount, self.field_aggregate_general_elec_expended, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_payee_committee_id_number, self.field_payee_candidate_id_number, self.field_payee_candidate_last_name, self.field_payee_candidate_first_name, self.field_payee_candidate_middle_name, self.field_payee_candidate_prefix, self.field_payee_candidate_suffix, self.field_payee_candidate_office, self.field_payee_candidate_state, self.field_payee_candidate_district, self.field_memo_code, self.field_memo_text_description],
              '^7.0|6.4' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_coordinated_expenditures, self.field_designating_committee_id_number, self.field_designating_committee_name, self.field_subordinate_committee_id_number, self.field_subordinate_committee_name, self.field_subordinate_street_1, self.field_subordinate_street_2, self.field_subordinate_city, self.field_subordinate_state, self.field_subordinate_zip_code, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_date, self.field_expenditure_amount, self.field_aggregate_general_elec_expended, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_payee_committee_id_number, self.field_payee_candidate_id_number, self.field_payee_candidate_last_name, self.field_payee_candidate_first_name, self.field_payee_candidate_middle_name, self.field_payee_candidate_prefix, self.field_payee_candidate_suffix, self.field_payee_candidate_office, self.field_payee_candidate_state, self.field_payee_candidate_district, self.field_memo_code, self.field_memo_text_description],
              '^6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_coordinated_expenditures, self.field_designating_committee_id_number, self.field_designating_committee_name, self.field_subordinate_committee_id_number, self.field_subordinate_committee_name, self.field_subordinate_street_1, self.field_subordinate_street_2, self.field_subordinate_city, self.field_subordinate_state, self.field_subordinate_zip_code, self.field_entity_type, self.field_payee_organization_name, self.field_payee_last_name, self.field_payee_first_name, self.field_payee_middle_name, self.field_payee_prefix, self.field_payee_suffix, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_expenditure_date, self.field_expenditure_amount, self.field_aggregate_general_elec_expended, self.field_expenditure_purpose_code, self.field_expenditure_purpose_descrip, self.field_category_code, self.field_increased_limit, self.field_payee_committee_id_number, self.field_payee_candidate_id_number, self.field_payee_candidate_last_name, self.field_payee_candidate_first_name, self.field_payee_candidate_middle_name, self.field_payee_candidate_prefix, self.field_payee_candidate_suffix, self.field_payee_candidate_office, self.field_payee_candidate_state, self.field_payee_candidate_district, self.field_memo_code, self.field_memo_text_description],
              '^5.3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_coordinated_expenditures, self.field_designating_committee_id_number, self.field_designating_committee_name, self.field_subordinate_committee_id_number, self.field_subordinate_committee_name, self.field_subordinate_street_1, self.field_subordinate_street_2, self.field_subordinate_city, self.field_subordinate_state, self.field_subordinate_zip_code, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_aggregate_general_elec_expended, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_payee_committee_id_number, self.field_payee_candidate_id_number, self.field_payee_candidate_name, self.field_payee_candidate_office, self.field_payee_candidate_state, self.field_payee_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text_description, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_increased_limit, self.field_category_code, self.field_expenditure_purpose_code],
              '^5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_coordinated_expenditures, self.field_designating_committee_id_number, self.field_designating_committee_name, self.field_subordinate_committee_id_number, self.field_subordinate_committee_name, self.field_subordinate_street_1, self.field_subordinate_street_2, self.field_subordinate_city, self.field_subordinate_state, self.field_subordinate_zip_code, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_aggregate_general_elec_expended, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_payee_committee_id_number, self.field_payee_candidate_id_number, self.field_payee_candidate_name, self.field_payee_candidate_office, self.field_payee_candidate_state, self.field_payee_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text_description, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name, self.field_increased_limit, self.field_category_code, self.field_expenditure_purpose_code],
              '^3' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_coordinated_expenditures, self.field_designating_committee_id_number, self.field_designating_committee_name, self.field_subordinate_committee_id_number, self.field_subordinate_committee_name, self.field_subordinate_street_1, self.field_subordinate_street_2, self.field_subordinate_city, self.field_subordinate_state, self.field_subordinate_zip_code, self.field_entity_type, self.field_payee_name, self.field_payee_street_1, self.field_payee_street_2, self.field_payee_city, self.field_payee_state, self.field_payee_zip_code, self.field_aggregate_general_elec_expended, self.field_expenditure_purpose_descrip, self.field_expenditure_date, self.field_expenditure_amount, self.field_payee_committee_id_number, self.field_payee_candidate_id_number, self.field_payee_candidate_name, self.field_payee_candidate_office, self.field_payee_candidate_state, self.field_payee_candidate_district, self.field_conduit_name, self.field_conduit_street_1, self.field_conduit_street_2, self.field_conduit_city, self.field_conduit_state, self.field_conduit_zip_code, None, self.field_transaction_id_number, self.field_memo_code, self.field_memo_text_description, self.field_back_reference_tran_id_number, self.field_back_reference_sched_name],
            },
            "^sl" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_record_id_number, self.field_account_name, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_itemized_receipts_persons, self.field_col_a_unitemized_receipts_persons, self.field_col_a_total_receipts_persons, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_voter_registration_disbursements, self.field_col_a_voter_id_disbursements, self.field_col_a_gotv_disbursements, self.field_col_a_generic_campaign_disbursements, self.field_col_a_disbursements_subtotal, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_receipts_period, self.field_col_a_subtotal_period, self.field_col_b_disbursements_period, self.field_col_b_cash_on_hand_close_of_period, self.field_col_b_itemized_receipts_persons, self.field_col_b_unitemized_receipts_persons, self.field_col_b_total_receipts_persons, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_voter_registration_disbursements, self.field_col_b_voter_id_disbursements, self.field_col_b_gotv_disbursements, self.field_col_b_generic_campaign_disbursements, self.field_col_b_disbursements_subtotal, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_beginning_period, self.field_col_b_receipts_period, self.field_col_b_subtotal_period, self.field_col_b_disbursements_period, self.field_col_b_cash_on_hand_close_of_period],
              '^5.3|5.2|5.1|5.0' : [ self.field_form_type, self.field_filer_committee_id_number, self.field_account_name, self.field_record_id_number, self.field_coverage_from_date, self.field_coverage_through_date, self.field_col_a_itemized_receipts_persons, self.field_col_a_unitemized_receipts_persons, self.field_col_a_total_receipts_persons, self.field_col_a_other_receipts, self.field_col_a_total_receipts, self.field_col_a_voter_registration_disbursements, self.field_col_a_voter_id_disbursements, self.field_col_a_gotv_disbursements, self.field_col_a_generic_campaign_disbursements, self.field_col_a_disbursements_subtotal, self.field_col_a_other_disbursements, self.field_col_a_total_disbursements, self.field_col_a_cash_on_hand_beginning_period, self.field_col_a_receipts_period, self.field_col_a_subtotal_period, self.field_col_b_disbursements_period, self.field_col_b_itemized_receipts_persons, self.field_col_b_unitemized_receipts_persons, self.field_col_b_total_receipts_persons, self.field_col_b_other_receipts, self.field_col_b_total_receipts, self.field_col_b_voter_registration_disbursements, self.field_col_b_voter_id_disbursements, self.field_col_b_gotv_disbursements, self.field_col_b_generic_campaign_disbursements, self.field_col_b_disbursements_subtotal, self.field_col_b_other_disbursements, self.field_col_b_total_disbursements, self.field_col_b_cash_on_hand_beginning_period, self.field_col_b_receipts_period, self.field_col_b_subtotal_period, self.field_col_b_disbursements_period, self.field_col_b_cash_on_hand_close_of_period, None, self.field_transaction_id_number],
            },
            "^text" : {
              '^8.0|7.0|6.4|6.3|6.2|6.1' : [ self.field_rec_type, self.field_filer_committee_id_number, self.field_transaction_id_number, self.field_back_reference_tran_id_number, self.field_back_reference_sched_form_name, self.field_text],
              '^5.3' : [ self.field_rec_type, self.field_form_type, self.field_back_reference_tran_id_number, self.field_text],
              '^5.2|5.1|5.0' : [ self.field_rec_type, self.field_form_type, self.field_back_reference_tran_id_number, self.field_text],
              '^3' : [ self.field_rec_type, self.field_form_type, self.field_back_reference_tran_id_number, self.field_text],
            },
          }

    
    def startHeader(self):
        self.state=STATE_HEADER
        print "start HEADER"
    
    def endHeader(self):
        print "END HEADER"
        self.state=STATE_BODY

    def HDR(self,l,quote=""):
        print "HEADER LINE",l, l.split(",")
        parts=l.split(",")
        header= parts[0]
        fec= parts[1]
        version= parts[2]
        #TODO use the new stuff
        # # source= parts[3]
        # # version2= parts[4]
        # # quote_row= parts[5]
        # # quote_row2= parts[6]
        # # quote_row3= parts[6]


    def delimiter(self,filing_version):
        if (filing_version.to_f < 6):
            return  "," 
        return "\034"

    def filing_url(self):
        return "http://query.nictusa.com/dcdev/posted/#{filing_id}.fec"


    def parse_file_data_line(self,l):
#        if re.match(r'\034',l):
        if l.find("\034") > 0:
            print "found 034 in %s" % l
            #if first.index("\034").nil?

        if re.match(r'\/\* Header',l):
            self.startHeader()
            return 

        if re.match(r'\/\* End Header',l):
            self.endHeader()
            return
        if re.match(r'HDR',l):
            self.HDR(l)
            return
        if re.match(r'\'HDR\'',l):
            self.HDR(l,quote='\'')
            return
        if re.match(r'\"HDR\"',l):
            self.HDR(l,quote='\"')
            return

        if self.state==STATE_HEADER :
            print "in header", l 
            return

        if self.state==STATE_BODY :
            print "in body", l 
            return

        print l
#                v=l.split("")              
#                self.generate(v,classname)
#                return


    def parse_file_data(self,d):
        for l in d.split("\n")[0:20]:
            self.parse_file_data_line(l)

    def generate(self,v,name):
        c=0
#        print "class %s:"  % name
        v2=[]
        v3=[]
        for f in v :
            f=f.strip(" ").rstrip(" ")
            f=f.strip("\"").rstrip("\"")
            #self.fields_dict[f]=c
            print "    %s=%d" % (f,c)
#            print "    def get%s(self):\n        return self.v[%s.%s]" % (f,name,f)            
            c=c+1
#            v2.append(f)       
#            v3.append("r.get%s()" % (f)) 
#        print "    fields=%s" % (v2)
#        print "    def printall(self):\n        print %s" % (",".join(v3))
