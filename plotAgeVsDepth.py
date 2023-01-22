import stratigraphy

site = stratigraphy.Site(1050, "A,C")

tiepoint0 = stratigraphy.Tiepoint(0, "pmag", "B C19n", 4.2, 11.23, 41.39)

tiepoint1 = stratigraphy.Tiepoint(1, "pmag", "B C19r", 24.14, 26.41, 42.30)

tiepoint2 = stratigraphy.Tiepoint(2, "pmag", "B C20n", 61.62, 62.19, 43.43)

tiepoint3 = stratigraphy.Tiepoint(3, "pmag", "B C20r", 137.27, 140.28, 45.72)

tiepoint4 = stratigraphy.Tiepoint(4, "pmag", "B C21n", 151.603, 153.190, 47.35)

tiepoint5 = stratigraphy.Tiepoint(5, "nanno", "B NP14a", 151.603, 153.190, 49.11)

tiepoint6 = stratigraphy.Tiepoint(6, "pmag", "B C22n", 153.71, 154.43, 49.34)

tiepoint7 = stratigraphy.Tiepoint(7, "pmag", "T C23n", 182.657, 183.359, 50.63)

tiepoint8 = stratigraphy.Tiepoint(8, "nanno", "B C. crassus", 193.2, 194.64, 51.64)

tiepoint9 = stratigraphy.Tiepoint(9, "nanno", "B NP12", 193.2, 194.64, 53.7)

tiepoint10 = stratigraphy.Tiepoint(10, "pmag", "B C24n", 198.37, 199.08, 53.98)

tiepoint11 = stratigraphy.Tiepoint(11, "pmag", " ", 198.37, 199.08, 53.98)


depths = [
                stratigraphy.average_depth(tiepoint0.min_depth, tiepoint0.max_depth),
                stratigraphy.average_depth(tiepoint1.min_depth, tiepoint1.max_depth),
                stratigraphy.average_depth(tiepoint2.min_depth, tiepoint2.max_depth),
                stratigraphy.average_depth(tiepoint3.min_depth, tiepoint3.max_depth),
                stratigraphy.average_depth(tiepoint4.min_depth, tiepoint4.max_depth),
                stratigraphy.average_depth(tiepoint5.min_depth, tiepoint6.max_depth),
                stratigraphy.average_depth(tiepoint7.min_depth, tiepoint7.max_depth),
                stratigraphy.average_depth(tiepoint8.min_depth, tiepoint8.max_depth),
                stratigraphy.average_depth(tiepoint9.min_depth, tiepoint9.max_depth),
                stratigraphy.average_depth(tiepoint10.min_depth, tiepoint10.max_depth),
                stratigraphy.average_depth(tiepoint11.min_depth, tiepoint11.max_depth)]

ages = [
                tiepoint0.age,
                tiepoint1.age,
                tiepoint2.age,
                tiepoint3.age,
                tiepoint4.age,
                tiepoint5.age,
                tiepoint6.age,
                tiepoint7.age,
                tiepoint8.age,
                tiepoint9.age,
                tiepoint10.age,
                tiepoint11.age
        ]

labels = [
                tiepoint0.label,
                tiepoint1.label,
                tiepoint2.label,
                tiepoint3.label,
                tiepoint4.label,
                tiepoint5.label,
                tiepoint6.label,
                tiepoint7.label,
                tiepoint8.label,
                tiepoint9.label,
                tiepoint10.label,
                tiepoint11.label
        ]

types = [
                tiepoint0.type,
                tiepoint1.type,
                tiepoint2.type,
                tiepoint3.type,
                tiepoint4.type,
                tiepoint5.type,
                tiepoint6.type,
                tiepoint7.type,
                tiepoint8.type,
                tiepoint9.type,
                tiepoint10.type,
                tiepoint11.type
        ]
