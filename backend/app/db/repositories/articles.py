'''
Michael Neilson <github: nichael-meilson>
2022-06-25
'''
from typing import List

from app.db.repositories.base import BaseRepository
from app.models.articles import CreateArticle, ArticleInDB, GetArticle

CREATE_ARTICLE_QUERY = """
    INSERT INTO articles (id, name, species, goal, num_lines, setup, recipient, medium, selective_condition, 
                          cripple_mutant, how_cripple_mutant, changing_env, how_changing_env, env_type, how_type_env, 
                          complex_stressors, how_complex_stressors, num_generations, abs_time, contamination, fitness, 
                          fitness_param, competition, mutation_tracking, wgs, wgs_tech, wgs_platform, num_clones, 
                          num_populations, cov_clones, cov_populations, detection_lim, ngs_data_link, max_pop_size, 
                          min_pop_size, major_outcome, remarks, complete_mutation_data, reference_id, pmid, paper_url)
    VALUES (:id, :name, :species, :goal, :num_lines, :setup, :recipient, :medium, :selective_condition, :cripple_mutant, 
            :how_cripple_mutant, :changing_env, :how_changing_env, :env_type, :how_type_env, :complex_stressors, 
            :how_complex_stressors, :num_generations, :abs_time, :contamination, :fitness, :fitness_param, :competition, 
            :mutation_tracking, :wgs, :wgs_tech, :wgs_platform, :num_clones, :num_populations, :cov_clones, 
            :cov_populations, :detection_lim, :ngs_data_link, :max_pop_size, :min_pop_size, :major_outcome, :remarks, 
            :complete_mutation_data, :reference_id, :pmid, :paper_url)
    RETURNING id, name, pmid, paper_url;
"""


class ArticlesRepository(BaseRepository):
    """"
    All database actions associated with the Article resource
    """

    async def create_article(self, *, new_article: CreateArticle) -> ArticleInDB:
        query_values = new_article.dict()
        created_article = await self.db.fetch_one(query=CREATE_ARTICLE_QUERY, values=query_values)
        return ArticleInDB(**created_article)

    async def get_all_articles(self) -> List[GetArticle]:
        get_articles_query = """SELECT * FROM articles ORDER BY name DESC"""
        all_articles = await self.db.fetch_all(query=get_articles_query)
        articles_list = [GetArticle(**article) for article in all_articles]
        return articles_list

