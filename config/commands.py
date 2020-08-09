
#  command example 'name':
#{
#    'answer': ' answer message',
#    'type': answer type, 1 - directed; 0 - non directed;
#    'media': 'media name - album id',
#},

sex = ''

def get_dict():

    dictionary_commands = {
        'default' :
        {
            'all':
            {
                'обнять':
                {
                    'answer': ' обнял%s ' %sex,
                    'type': 1,
                    'media': 272136362,
                },

                'поцеловать':
                {
                    'answer': ' поцеловал%s ' %sex,
                    'type': 1,
                    'media': 272136370,
                },

                'ударить':
                {
                    'answer': ' ударил%s ' %sex,
                    'type': 1,
                    'media': 272136375,
                },

                'надуться':
                {
                    'answer': ' надул%s щёчки' %sex,
                    'type': 0,
                    'media': 272136355,
                },

                'ебать никиту':
                {
                    'answer': 'Я выебала Никиту',
                    'type': 0,
                    'media': None,
                },

                'накормить':
                {
                    'answer': ' накормил%s ' %sex,
                    'type': 1,
                    'media': 272136359,
                },

                'покормить':
                {
                    'answer': ' покормил%s ' %sex,
                    'type': 1,
                    'media': 272136359,
                },

                'связать':
                {
                    'answer': ' связал%s ' %sex,
                    'type': 1,
                    'media': 272136372,
                },

                'привет':
                {
                    'answer': ' поприветствовал%s ' %sex,
                    'type': 1,
                    'media': 272151185,
                },

                'q':
                {
                    'answer': ' поприветствовал%s ' %sex,
                    'type': 1,
                    'media': 272151185,
                },

                'кусь':
                {
                    'answer': ' укусил%s ' %sex,
                    'type': 1,
                    'media': 272173642,
                },

                'погладить':
                {
                    'answer': ' погладил%s ' %sex,
                    'type': 1,
                    'media': 272178874,
                },

                'посадить на коленочки' :
                {
                    'answer': ' посадил%s на коленочки' %sex,
                    'type': 1,
                    'media': 272178865,
                },

                'потискать за щёчки':
                {
                    'answer': ' потискал%s за щёчки' %sex,
                    'type': 1,
                    'media': 272178882,
                },

                'потискать за щечки':
                {
                    'answer': ' потискал%s за щёчки' %sex,
                    'type': 1,
                    'media': 272178882,
                },

                'послать сердечко':
                {
                    'answer': ' послал%s сердечко' %sex,
                    'type': 1,
                    'media': 272178918,
                },

                'рычать':
                {
                    'answer': ' рычит',
                    'type': 0,
                    'media': 272178943,
                },

                'смутиться':
                {
                    'answer': ' смущен%s',
                    'type': 0,
                    'media': 272178945,
                },

                'лизь':
                {
                    'answer': ' лизнул%s ' %sex,
                    'type': 1,
                    'media': 272178947,
                },

                'прижать':
                {
                    'answer': ' прижал%s ' %sex,
                    'type': 1,
                    'media': 272178949,
                },

                'взять за ручку':
                {
                    'answer': ' взял%s за ручку' %sex,
                    'type': 1,
                    'media': 272178950,
                },

                'облапать':
                {
                    'answer': ' облапал%s ' %sex,
                    'type': 1,
                    'media': 272178975,
                },

                'посадить на цепь':
                {
                    'answer': ' посадил%s на цепь' %sex,
                    'type': 1,
                    'media': 272197731,
                },

                'поцеловать в щёчку':
                {
                    'answer': ' поцеловал%s в щёчку' %sex,
                    'type': 1,
                    'media': 272972761,
                },

                'поцеловать в щечку':
                {
                    'answer': ' поцеловал%s в щёчку' %sex,
                    'type': 1,
                    'media': 272972761,
                },

                'обнять всех':
                {
                    'answer': ' обнял%s всех',
                    'type': 0,
                    'media': 273013062,
                },

                'обнять алл':
                {
                    'answer': ' обнял%s всех',
                    'type': 0,
                    'media': 273013062,
                },

                'подрочить':
                {
                    'answer': ' подрочил%s',
                    'type': 0,
                    'media': None,
                },

                'посасать':
                {
                    'answer': ' посасал%s',
                    'type': 0,
                    'media': None,
                },

                'грустить':
                {
                    'answer': ' грустит',
                    'type': 0,
                    'media': 272171414,
                },

            },

            'admins':
            {
                'off':
                {
                    'answer': ' я выключена',
                    'type': 0,
                    'media': None,
                },

                'on':
                {
                    'answer': ' я включена',
                    'type': 0,
                    'media': None,
                },

                'kick':
                {
                    'answer': ' я выключена',
                    'type': 1,
                    'media': None,
                },

                'кик':
                {
                    'answer': ' я выключена',
                    'type': 1,
                    'media': None,
                },
            },

            'father':
            {

            },

            'married':
            {

            },

            'music':
            {

            },
        },

        '0':
        {
            'all':
            {
                'пошёл':
                {
                    'answer': ' пошёл%s на хуй' %sex,
                    'type': 1,
                    'media': 272136362,
                },
            }
        },



    }

    return dictionary_commands
