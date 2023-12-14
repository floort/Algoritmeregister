import pandas as pd
from typing import Literal
import app.config.config as configuration


class Transformer:
    def __init__(self, json: list[dict]):
        self.json = json
        self.df_organisation_columns = configuration.df_organisation_columns
        self.df_algoritme_columns = configuration.df_algoritme_columns
        self.df_algoritme_version_columns = configuration.df_algoritme_version_columns

    def json_to_df(
        self, table_name: Literal["algoritme", "algoritme_version", "organisation"]
    ):
        match table_name:
            case "organisation":
                return self.get_organisation_df()
            case "algoritme":
                return self.get_algoritme_df()
            case "algoritme_version":
                return self.get_algoritme_version_df()

    def get_organisation_df(self) -> pd.DataFrame:
        df = pd.DataFrame(self.json)[self.df_organisation_columns].copy()

        df.drop_duplicates(subset="owner", keep="first", inplace=True)
        df = df.reset_index(drop=True).reset_index()
        df.rename(
            columns={"index": "id", "owner": "code", "organization": "name"},
            inplace=True,
        )
        self.df_organisation = df
        return self.df_organisation

    def get_algoritme_df(self) -> pd.DataFrame:
        # Should be based on df_organisation... is not yet
        df = pd.DataFrame(self.json)[[*self.df_algoritme_columns, "owner"]].copy()

        # The column rename allows merging.
        df.rename(columns={"owner": "code"}, inplace=True)
        merged_df = pd.merge(self.df_organisation, df, on="code", how="inner")

        # Clean-up merge
        merged_df.rename(columns={"id": "organisation_id"}, inplace=True)
        merged_df.drop(["code", "name"], axis=1, inplace=True)

        # Have an explicit id column, because it is a foreign key. So you need to be able to merge with it.
        merged_df.reset_index(inplace=True)
        merged_df.rename(columns={"index": "id"}, inplace=True)
        self.df_algoritme = merged_df
        return self.df_algoritme

    def get_algoritme_version_df(self) -> pd.DataFrame:
        df = pd.DataFrame(self.json)

        #  Column 'lars' is needed to match foreign keys.
        df = df[[*self.df_algoritme_version_columns, "lars"]].copy()

        # Add id from the df_algoritme to this df as foreign key.
        merged_df = pd.merge(self.df_algoritme, df, on="lars", how="inner")
        merged_df.rename(
            columns={"id": "algoritme_id", "create_dt_x": "create_dt"}, inplace=True
        )
        merged_df.drop(["lars", "create_dt_y", "organisation_id"], axis=1, inplace=True)
        merged_df["language"] = "NLD"
        return merged_df
