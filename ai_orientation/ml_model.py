from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

SPECIALTIES_DATA = {
    'Cardiologie': [
        'douleur poitrine palpitations essoufflement coeur cardiaque',
        'tachycardie hypertension infarctus angine thorax',
    ],
    'Dermatologie': [
        'peau boutons rougeurs démangeaisons eczéma acné',
        'éruption cutanée taches urticaire psoriasis allergie peau',
    ],
    'Pédiatrie': [
        'enfant fièvre bébé nourrisson vaccination croissance',
        'otite angine enfant toux pediatre développement',
    ],
    'Gynécologie': [
        'grossesse règles menstruation utérus ovaires femme',
        'contraception fertilité gynécologique douleur pelvienne',
    ],
    'Neurologie': [
        'maux de tête migraine vertiges convulsions neurologique',
        'paralysie tremblement épilepsie sclérose cerveau',
    ],
    'Ophtalmologie': [
        'yeux vue vision trouble ophtalmique lunettes',
        'conjonctivite cataracte glaucome oeil douleur oculaire',
    ],
    'ORL': [
        'oreille nez gorge angine sinusite rhume audition',
        'tonsillite otite laryngite pharyngite rhinite',
    ],
    'Dentisterie': [
        'dent douleur dentaire carie gencive mâchoire',
        'extraction dentiste prothèse mal dents',
    ],
    'Médecine générale': [
        'fatigue fièvre grippe rhume ordonnance généraliste',
        'consultation générale mal général bilan santé',
    ],
    'Radiologie': [
        'radio scanner IRM imagerie radiographie échographie',
        'examen radiologique diagnostic image médicale',
    ],
}

def get_specialty_recommendations(symptom_text, top_n=3):
    """Analyse les symptômes et retourne les spécialités recommandées."""
    if not symptom_text or not symptom_text.strip():
        return []

    corpus = []
    specialty_names = []

    for specialty, descriptions in SPECIALTIES_DATA.items():
        combined = ' '.join(descriptions)
        corpus.append(combined)
        specialty_names.append(specialty)

    try:
        vectorizer = TfidfVectorizer(
            analyzer='word',
            ngram_range=(1, 2),
        )
        tfidf_matrix = vectorizer.fit_transform(corpus)
        query_vec = vectorizer.transform([symptom_text.lower()])
        similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
        top_indices = np.argsort(similarities)[::-1][:top_n]

        results = []
        for idx in top_indices:
            if similarities[idx] > 0.01:
                results.append({
                    'specialty': specialty_names[idx],
                    'score': round(float(similarities[idx]) * 100, 1)
                })
        return results

    except Exception as e:
        return []