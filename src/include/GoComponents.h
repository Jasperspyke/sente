//
// Created by arthur wesley on 7/2/21.
//

#ifndef SENTE_COMPONENTS_H
#define SENTE_COMPONENTS_H

#include <sstream>

#include "Board.h"
#include "Move.h"

#ifdef __MINGW32__
#include <ciso646>
#endif

namespace sente {

    enum Rules {
        CHINESE,
        JAPANESE
    };

    double getKomi(Rules ruleset);

    struct Results{

        explicit Results(Stone resigningPlayer);

        Results(Rules rules, double komi, unsigned blackTerritory, unsigned whiteTerritory,
                       unsigned blackStones, unsigned whiteStones);

        Stone winner() const;
        double margin() const;

        Rules rules;
        double komi;

        unsigned blackScore;
        unsigned whiteScore;

        Stone resignedPlayer;

        operator std::string() const;

    };

}

#endif //SENTE_COMPONENTS_H
