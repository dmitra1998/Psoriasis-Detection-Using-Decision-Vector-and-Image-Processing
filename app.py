from src.Database import Database
from src.dbop import Dbop

__author___ = 'sdas'

from flask import Flask, render_template, request, session
import string

app = Flask(__name__)  # '__main__'
d = {}


@app.route('/')  # www.mywebsite.com/api/
def hello_method():
    return render_template('base.html')


@app.route('/result', methods=['POST'])
def decision_method():
    d[1] = request.form['d1']
    d[2] = request.form['d2']
    d[3] = request.form['d3']
    d[4] = request.form['d4']
    d[5] = request.form['d5']
    d[6] = request.form['d6']
    d[7] = request.form['d7']
    d[8] = request.form['d8']
    d[91] = request.form['d9a']
    d[92] = request.form['d9b']
    d[10] = request.form['d10']
    d[111] = request.form['d11a']
    d[112] = request.form['d11b']
    d[113] = request.form['d11c']

    s = ""
    decision = ""
    cause = ""
    treatment = ""
    heredity = ""
    g1=0
    g2=0

    for i in d.values():
        s = s + i
    print(s)
    x = Database.find_one(collection='Db', query=s)
    if x is None:
        if d[1] == '1':
            if d[2] == '1':
                print("Both Parents have psoriasis")
                h = "50% risk of having psoriasis due to heredity link"
                g1 = 1
            else:
                print("Single parent have psoriasis")
                h = "10% risk of having psoriasis due to heredity link"
                g1 = 2

        if d[3] == '1':
            print("Siblings have psoriasis")
            h = "4 to 6 times more likely to have psoriasis compared with the general population due to heredity link"
            g1 = 3

        if d[1] == '0' and d[2] == '0' and d[3] == '0':
            g1 = 4
            h = "No heredity link found which will effect the chances for psoriasis"

        if d[4] == '1':
            if d[7] == '1':
                g2 = 9
                decision = "Nail psoriasis"
                cause = "Caused due to excessive growth of skin cells,or thickening of skin cells,also due to skin inflammation and sometimes due to the result of psoriatic arthritis"
                treatment = "It may take time to see the effects of these treatments as nails grow very slowly. Treatment options include:\n1)light therapy\n2)Oral medications, such as methotrexate.\n3)Biological causes which are available via injection or intravenous infusion. "
                heredity = h

            else:
                if d[8] == '1':
                    g2 = 10
                    decision = "Scalp psoriasis"
                    cause = "Caused due to plaque psoriasis ,can happen due to smoking,lack of vitamin-D."
                    treatment = "1)Opical treatments are most commonly used for scalp psoriasis. They may require an initial two months of intensive applications, plus permanent, regular maintenance.\n2)Medicated shampoos\n3)Steroid-containing lotions\n4)Tar preparation\n5)Topical application of vitamin D, known as calcipotriene (Dovonex)."
                    heredity = h

                else:
                    g2 = 1
                    decision = "Plaque psoriasis"
                    cause = "Caused due to hereditary link with the disease and also due to excessive stress."
                    treatment = "1)Applying moisturizers to keep the skin from becoming too dry or irritated.\n 2)Vitamin D creams, such as calcipotriene (Dovonex) and calcitrol (Rocaltrol) to reduce the rate that skin cells grow.\n3)Topical retinoids, to help reduce inflammation.\n4)Medication like tazarotene (Tazorac, Avage).\n5)Applications of coal tar, either by cream, oil, or shampoo."
                    heredity = h


        elif d[5] == '1':
            if d[7] == '1':
                g2 = 9
                decision = "Nail psoriasis"
                cause = "caused due to excessive growth of skin cells,or thickening of skin cells,also due to skin inflammation and sometimes due to the result of psoriatic arthritis"
                treatment = "It may take time to see the effects of these treatments as nails grow very slowly. Treatment options include:\n1)light therapy\n2)Oral medications, such as methotrexate.\n3)Biological causes which are available via injection or intravenous infusion. "
                heredity = h

            else:
                if d[8] == '1':
                    g2 = 10
                    decision = "Scalp psoriasis"
                    cause = "Caused due to plaque psoriasis ,can happen due to smoking,lack of vitamin-D."
                    treatment = "1)Opical treatments are most commonly used for scalp psoriasis. They may require an initial two months of intensive applications, plus permanent, regular maintenance.\n2)Medicated shampoos\n3)Steroid-containing lotions\n4)Tar preparation\n5)Topical application of vitamin D, known as calcipotriene (Dovonex)."
                    heredity = h

                else:
                    g2 = 2
                    decision = "Guttate psoriasis"
                    cause = "Caused due to upper respiratory infections,streptococcal infection,stress,use of drugs(such as antimarals,lithum,beta-blockers), bacterial infection such as strep throat,skin injury and also due to stress."
                    treatment = "1)Condition-antibiotics may help\n2)Steroid creams,light therapy and oral meditation"
                    heredity = h

        elif d[6] == '1':
            if d[7] == '1':
                g2 = 9
                decision = "Nail psoriasis"
                cause = "caused due to excessive growth of skin cells,or thickening of skin cells,also due to skin inflammation and sometimes due to the result of psoriatic arthritis"
                treatment = "It may take time to see the effects of these treatments as nails grow very slowly. Treatment options include:\n1)light therapy\n2)Oral medications, such as methotrexate.\n3)Biological causes which are available via injection or intravenous infusion. "
                heredity = h

            else:
                if d[8] == '1':
                    g2 = 10
                    decision = "Scalp psoriasis"
                    cause = "Caused due to plaque psoriasis ,can happen due to smoking,lack of vitamin-D."
                    treatment = "1)Opical treatments are most commonly used for scalp psoriasis. They may require an initial two months of intensive applications, plus permanent, regular maintenance.\n2)Medicated shampoos\n3)Steroid-containing lotions\n4)Tar preparation\n5)Topical application of vitamin D, known as calcipotriene (Dovonex)."
                    heredity = h

                else:
                    g2 = 3
                    decision = "Fluxtural or inverse psoriasis"
                    cause = "Caused mostly due to fungal infections , deep skin folds and obesity."
                    treatment = "1)Topical steroid creams, light therapy, and oral medications.\n2)Taking or applying medications that reduce yeast or bacteria growth."
                    heredity = h


        elif d[91] == '1' and d[92] == '1':
            if d[10] == '1':
                g2 = 8
                decision = "Erythrodemic psoriasis"
                cause = "Caused due to unstable plaque psoriasis, imbalance in homeostosis,and also due to alcholism."
                treatment = "1)A person with this condition often needs hospital attention. At the hospital, you’ll receive a combination of therapies.\n2)•	This can include an application of medicated wet dressings, topical steroid applications, and prescription oral medications until symptoms have improved.\n3)Make an appointment with your doctor"
                heredity = h

            elif d[7] == '1':
                g2 = 9
                decision = "Nail psoriasis"
                cause = "caused due to excessive growth of skin cells,or thickening of skin cells,also due to skin inflammation and sometimes due to the result of psoriatic arthritis"
                treatment = "It may take time to see the effects of these treatments as nails grow very slowly. Treatment options include:\n1)light therapy\n2)Oral medications, such as methotrexate.\n3)Biological causes which are available via injection or intravenous infusion. "
                heredity = h

            elif d[8] == '1':
                g2 = 10
                decision = "Scalp psoriasis"
                cause = "Caused due to plaque psoriasis ,can happen due to smoking,lack of vitamin-D."
                treatment = "1)Opical treatments are most commonly used for scalp psoriasis. They may require an initial two months of intensive applications, plus permanent, regular maintenance.\n2)Medicated shampoos\n3)Steroid-containing lotions\n4)Tar preparation\n5)Topical application of vitamin D, known as calcipotriene (Dovonex)."
                heredity = h

            else:
                g2 = 4
                decision = "Pustural psoriasis"
                cause = "Caused due to certain drugs like pencellin,sunburn and also due to excessive stress."
                treatment = "1)Smaller patches are often treated with corticosteroid creams, either OTC or prescription. Larger patches may need treatment with oral medications and light therapy.\n2)These topical preparations containing a synthetic form of vitamin A can help improve psoriasis. These preparations don't work as quickly as steroids. Topical retinoids can sometimes cause dryness and irritation of the skin."
                heredity = h

        elif d[111] == '1':
            if d[112] == '1':
                g2 = 5
                decision = "Symmetric Psoriatic arthritis psoriasis"
                cause = "Caused due to heredity link,injuries to skin,also sometimes due to excessive streaching."
                treatment = "1)Nonsteroidal anti-inflammatory drugs (NSAIDs), such as ibuprofen (Advil) and naproxen sodium (Aleve) can help reduce the incidences of swelling and pain associated with symmetric psoriatic arthritis.\n2)Light therapy may also help reduce symptoms.\n3)Prescription topical medications used to treat psoriatic arthritis include salicylic acid, calciopotriene, and tazarotene."
                heredity = h

            if d[113] == '1':
                g2 = 6
                decision = "Asymmetric Psoriatic arthritis psoriasis"
                cause = "Caused due to skin inflammation,skin infection,intake of certain drugs"
                treatment = "1)Treatment for psoriatic arthritis consists of twice daily moist heat or cold applications, exercises, and nonsteroidal anti-inflammatory drugs (NSAIDs).\n2)If there is little improvement or if there are permanent changes visible on an X-ray, then a disease-modifying antirheumatic drug (DMARD) or a biologic drug will be added to help prevent long-term joint damage.\n3)Enzyme inhibitors such as apremilast (Otezla) can also be prescribed to block proteins that cause the inflammation."
                heredity = h

            if d[112] == '0' and d[113] == '0':
                g2 = 7
                decision = "Psoriatic arthritis psoriasis"
                cause = "Caused due to injury in skin,sunburn,hormonal changes,excessive smoking and also linked to heredity."
                treatment = "1)Nonsteroidal anti-inflammatory drugs (NSAIDs), such as ibuprofen (Advil) and naproxen sodium (Aleve) can help reduce the incidences of swelling and pain associated with symmetric psoriatic arthritis.\n2)Light therapy may also help reduce symptoms.\n3)Prescription topical medications used to treat psoriatic arthritis include salicylic acid, calciopotriene, and tazarotene."
                heredity = h

        elif d[10] == '1':
            if d[7] == '1':
                g2 = 9
                decision = "Nail psoriasis"
                cause = "caused due to excessive growth of skin cells,or thickening of skin cells,also due to skin inflammation and sometimes due to the result of psoriatic arthritis"
                treatment = "It may take time to see the effects of these treatments as nails grow very slowly. Treatment options include:\n1)light therapy\n2)Oral medications, such as methotrexate.\n3)Biological causes which are available via injection or intravenous infusion. "
                heredity = h

            elif d[8] == '1':
                g2 = 10
                decision = "Scalp psoriasis"
                cause = "Caused due to plaque psoriasis ,can happen due to smoking,lack of vitamin-D."
                treatment = "1)Opical treatments are most commonly used for scalp psoriasis. They may require an initial two months of intensive applications, plus permanent, regular maintenance.\n2)Medicated shampoos\n3)Steroid-containing lotions\n4)Tar preparation\n5)Topical application of vitamin D, known as calcipotriene (Dovonex)."
                heredity = h

            else:
                g2 = 8
                decision = "Erythrodemic psoriasis"
                cause = "Caused due to unstable plaque psoriasis, imbalance in homeostosis,and also due to alcholism."
                treatment = "1)A person with this condition often needs hospital attention. At the hospital, you’ll receive a combination of therapies.\n2)•	This can include an application of medicated wet dressings, topical steroid applications, and prescription oral medications until symptoms have improved.\n3)Make an appointment with your doctor"
                heredity = h

        elif d[7] == '1':
            g2 = 9
            decision = "Nail psoriasis"
            cause = "caused due to excessive growth of skin cells,or thickening of skin cells,also due to skin inflammation and sometimes due to the result of psoriatic arthritis"
            treatment = "It may take time to see the effects of these treatments as nails grow very slowly. Treatment options include:\n1)light therapy\n2)Oral medications, such as methotrexate.\n3)Biological causes which are available via injection or intravenous infusion. "
            heredity = h

        elif d[8] == '1':
            g2 = 10
            decision = "Scalp psoriasis"
            cause = "Caused due to plaque psoriasis ,can happen due to smoking,lack of vitamin-D."
            treatment = "1)Opical treatments are most commonly used for scalp psoriasis. They may require an initial two months of intensive applications, plus permanent, regular maintenance.\n2)Medicated shampoos\n3)Steroid-containing lotions\n4)Tar preparation\n5)Topical application of vitamin D, known as calcipotriene (Dovonex)."
            heredity = h

        else:
            g2 = 11
            decision = "Psoriasis not found"
            cause = "Consult doctor"
            treatment = "Consult doctor"
            heredity = h

        dbop = Dbop(s, g1, g2, decision, cause, treatment, heredity)
        dbop.insert_to_database()
        return render_template('result.html', decision=decision, cause=cause, treatment=treatment, heredity=h)
    else:
        return render_template('result.html', decision=x['Type'], cause=x['Cause'], treatment=x['Treatment'], heredity=x['Heredity'])



if __name__ == '__main__':
    Database.initialize()
    app.run(port=4995)
