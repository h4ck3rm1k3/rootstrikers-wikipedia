
    # self.base_row_types = ["HDR", "F1", "F13", "F132", "F133", "F1M",
    #         "F2", "F24", "F3", "F3L", "F3P", "F3P31", "F3PS", "F3S", "F3X",
    #         "F4", "F5", "F56", "F57", "F6", "F65", "F7", "F76", "F9", "F91",
    #         "F92", "F93", "F94", "F99", "H1", "H2", "H3", "H4", "H5", "H6",
    #         "SchA", "SchB", "SchC", "SchC1", "SchC2", "SchD", "SchE", "SchF",
    #         "SchL", "TEXT"]

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

class Rows :
    def __init__(self):
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

    def row_type_hdr(self):
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
