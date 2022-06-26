'''
Michael Neilson <github: nichael-meilson>
2022-06-18
'''
from typing import Optional
from enum import Enum

import pydantic

from app.models.core import IDModelMixin


class ArticleGoal(str, Enum):
    EVOLUTION = "Study Evolution(ary Processes)"
    TRAITS = "Study Complex Traits"
    STRAINS = "Improve Strains"


class ArticleBase(IDModelMixin):
    name: str = pydantic.Field(..., description="Name of the author & publishing year")
    species: str = pydantic.Field(..., description="Latin name of species. If multiple, separate by ';'")
    goal: ArticleGoal = pydantic.Field(..., description="Goal of the experiment")
    num_lines: int = pydantic.Field(..., description="Number of parallel evolved populations")
    setup: str = pydantic.Field(..., description="Basic setup used to accumulate generations")
    recipient: str = pydantic.Field(..., description="Physical receiver housing experiment in the lab")
    medium: str = pydantic.Field(..., description="Medium the experiment was suspended in")
    selective_condition: str = pydantic.Field(..., description="Selective pressure(s) applied")
    cripple_mutant: bool = pydantic.Field(..., description="Was a significantly impaired mutant used?")
    how_cripple_mutant: Optional[str] = pydantic.Field(..., description="How was the mutant crippled?")
    changing_env: bool = pydantic.Field(..., description="Did environment change over time?")
    how_changing_env: Optional[str] = pydantic.Field(..., description="How did the environment change?")
    env_type: str = pydantic.Field(..., description="Structured or heterogeneous environment? Was it not well mixed?")
    how_type_env: str = pydantic.Field(..., description="How was it structured/heterogeneous? e.g. on a biofilm...")
    complex_stressors: bool = pydantic.Field(..., description="Are there multiple stressors in the environment?")
    how_complex_stressors: str = pydantic.Field(..., description="Which stressors are in the environment?")
    num_generations: int = pydantic.Field(..., description="Estimated number of generations in experiment")
    abs_time: int = pydantic.Field(..., description="Number of days experiment took place")
    contamination: str = pydantic.Field(..., description="How was contamination checked for?")
    fitness: bool = pydantic.Field(..., description="Was fitness determined?")
    fitness_param: Optional[str] = pydantic.Field(..., description="How was fitness determined?")
    competition: Optional[str] = pydantic.Field(..., description="What competition was measured?")
    mutation_tracking: Optional[str] = pydantic.Field(..., description="How was mutation tracked?")
    wgs: bool = pydantic.Field(..., description="Was whole genome sequencing performed?")
    wgs_tech: str = pydantic.Field(..., description="What tech was used for WGS?")
    wgs_platform: str = pydantic.Field(..., description="What WGS platform?")
    num_clones: int = pydantic.Field(..., description="How many clones sequenced?")
    num_populations: int = pydantic.Field(..., description="How many populations sequenced?")
    cov_clones: float = pydantic.Field(..., description="What was the coverage of clonal data?")
    cov_populations: float = pydantic.Field(..., description="What was the coverage of population data?")
    detection_lim: float = pydantic.Field(..., description="Population sequencing: what was the detection limit \
                                                            of mutations?")
    ngs_data_link: str = pydantic.Field(..., description="URL of NGS data")
    max_pop_size: int = pydantic.Field(..., description="Max size of population")
    min_pop_size: int = pydantic.Field(..., description="Min size of population")
    major_outcome: str = pydantic.Field(..., description="What was the main takeaway/result of the experiment?")
    remarks: str = pydantic.Field(..., description="Anything else to note in the entry?")
    complete_mutation_data: bool = pydantic.Field(..., description="Is there existing mutation data \
                                                                    for the experiment?")
    reference_id: str = pydantic.Field(..., description="Format: [Authors, separated by commas];title;\
                                                            year;volume;page-page")
    pmid: str = pydantic.Field(..., description="Pubmed ID")
    paper_url: str = pydantic.Field(..., description="URL to paper")


class CreateArticle(ArticleBase):
    pass


class GetArticle(ArticleBase):
    pass


class ArticleInDB(IDModelMixin):
    name: str
    pmid: str
    paper_url: str