import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def run_tech_stack_recommender():
    print("==================================================================")
    print("DECODELABS ACTIVE PREDICTION SUITE: MATCHMAKER RECON ENGINE")
    print("Batch: 2026 | Project 3: AI Recommendation Logic")
    print("==================================================================\n")

    career_dataset = {
        "Data Scientist": "python sql machine learning data analysis predictive modeling statistics pandas engineering",
        "DevOps Engineer": "aws docker kubernetes cicd automation linux shell scripting cloud git systems",
        "Backend Developer": "java python sql apis databases django spring boot rest microservices architecture git",
        "Frontend Developer": "javascript react angular html css typescript vue web design ui ux responsive frontend",
        "Data Engineer": "sql python spark cloud big data pipelines logging database modeling etl storage scala",
        "Cloud Architect": "aws azure cloud computing security enterprise systems architecture networking terraform infrastructure",
        "Cybersecurity Analyst": "networking security firewalls pentesting linux protocol encryption threat analysis tracking",
        "AI Research Engineer": "python tensorflow pytorch deep learning transformers computer vision nlp math research algorithms"
    }

    job_roles = list(career_dataset.keys())
    skill_documents = list(career_dataset.values())

    tfidf_vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b[\w-]+\b')
    tfidf_matrix = tfidf_vectorizer.fit_transform(skill_documents)
    global_vocabulary = tfidf_vectorizer.get_feature_names_out()

    print(f"-> Similarity Processing Core Engine successfully initialized.")
    print(f"-> Ingested {len(job_roles)} distinct operational vectors out of source metadata profiles.")
    print(f"-> Mathematical Vector space dimension mapped to: {len(global_vocabulary)} target tokens.\n")

    print("[FEATURE 1 & 2] Initiating Structural Onboarding Questionnaire...")
    print("-> Please specify professional technical credentials to bootstrap baseline vector.")
    print("-> Type 'exit' at any parameter checkpoint to close the engine instance.\n")

    user_skills = []
    input_index = 1

    while len(user_skills) < 3:
        user_input = input(f"Enter Key Skill Coordinate #{input_index}: ").strip().lower()
        
        if user_input == 'exit':
            print("\nSession execution terminated safely via terminal request command.")
            return
            
        if not user_input:
            print("[WARNING] Vector field cannot be empty. Ingest valid alphanumeric input.")
            continue

        if user_input not in global_vocabulary:
            print(f"[VOCABULARY OUTLIER] Note: '{user_input}' is outside current career map indexes.")
            print("  Continuing will evaluate vector alignment across matching overlapping criteria.\n")
            
        user_skills.append(user_input)
        input_index += 1

    print("\n[FEATURE 3] Launching Live Digital Matchmaker Engine...")
    user_profile_string = " ".join(user_skills)
    user_vector = tfidf_vectorizer.transform([user_profile_string])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()

    if np.all(similarity_scores == 0):
        print("\n[COLD START DETECTED] No direct structural token intersections found.")
        print("-> Activating Trending Fallback Protocol (Routing to universal benchmark options).")
        recommended_indices = [0, 1, 2] 
        final_scores = [0.0, 0.0, 0.0]
    else:
        recommended_indices = np.argsort(similarity_scores)[::-1][:3]
        final_scores = [similarity_scores[idx] for idx in recommended_indices]

    print("\n=================== CHOSEN VERDICT MATCH DATA ===================")
    print("Rank | Recommended Professional Track  | Confidence Profile Alignment")
    print("-----------------------------------------------------------------")
    
    output_roles = []
    output_percentages = []
    
    for i, idx in enumerate(recommended_indices):
        rank = i + 1
        role_name = job_roles[idx]
        match_percentage = final_scores[i] * 100
        
        output_roles.append(role_name)
        output_percentages.append(match_percentage)
        
        print(f" #{rank}  | {role_name:<31} | {match_percentage:^26.2f}%")
    print("=================================================================\n")

    print("[FEATURE 4] Generating Multi-Dimensional Alignment Bar Chart Visual...")
    
    plt.figure(figsize=(9, 4.5))
    y_pos = np.arange(len(output_roles))
    
    bars = plt.barh(y_pos, output_percentages[::-1], color='#3a86ff', edgecolor='#03045e', height=0.5)
    
    plt.yticks(y_pos, output_roles[::-1], fontsize=10, fontweight='bold')
    plt.xlabel('Mathematical Vector Alignment Level (%)', fontsize=11, fontweight='bold', labelpad=10)
    plt.title('DecodeLabs AI Matchmaker Analytics: Top-3 Career Proximity Vectors', fontsize=13, fontweight='bold', pad=15)
    plt.xlim(0, 106)
    plt.grid(axis='x', linestyle='--', alpha=0.5)

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1.5, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', 
                 va='center', ha='left', fontsize=10, fontweight='bold', color='#1d3557')

    plt.tight_layout()
    print("-> Data visualization frame successfully computed. Rendering visualization display window now.")
    plt.show()

if __name__ == "__main__":
    run_tech_stack_recommender()
