from services.basic_text_analysis import basic_text_stats


def ARI(context):
    stats = basic_text_stats(context)
    ari_score = 4.71 * (len(stats["characters"]) / len(stats["words"])) + 0.5 * \
        (len(stats["words"]) / len(stats["sentences"])) - 21.43
    return ari_score


def flesch_kincaid(context):
    stats = basic_text_stats(context)
    fk_score = 0.39 * (len(stats["words"]) / len(stats["sentences"])) + \
        11.8 * (stats["syllablecount"] / len(stats["words"])) - 15.59
    return fk_score
