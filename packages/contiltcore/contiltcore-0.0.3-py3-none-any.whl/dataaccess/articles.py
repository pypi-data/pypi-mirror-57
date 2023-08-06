from .database import Database
class Articles():

    def __init__(self, config):
        self.database = Database(config)

    def get_query(self, lang, start, end, randomizationseed, status):
        query = "SELECT atitle as title, abody as text FROM sitearticles where astatus='" + status + "'"
        if lang is not None:
            query += " AND alanguage='" + lang + "'"
        if randomizationseed is not None:
            query += " ORDER BY id % " + str(randomizationseed)
        if (start is not None) and (end is not None):
            query += " limit " + str(start) + "," + str(end)

        return query


    def add_articles(self, articles):
        db = self.database.conn()
        cur = db.cursor()
        datatoinsert = list(map(lambda a:
                                [a["asite"], a["atitle"], a["abody"], a["aurl"], a["atags"], a["astatus"],
                                 a["projectid"], a["alanguage"]]
                                , articles))

        cur.executemany(
            "INSERT IGNORE INTO sitearticles (asite, atitle, abody, aurl, atags, astatus, projectid, alanguage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ",
            datatoinsert)
        db.commit()
        cur.close()
        db.close()

    def get_articles(self, lang, start, end,randomizationseed=None, status="RAW"):
        return self.database.executequery(Articles.get_query(lang, start, end, randomizationseed, status))

    def get_dataset_size(self, datasetgenerator, lang, start, end, randomizationseed=None, status="RAW"):
        size = 0
        db = self.database.conn()
        cur = db.cursor()
        cur.execute(Articles.get_query(lang, start, end, randomizationseed, status))
        for data in cur:
            article = {}
            for i in range(len(data)): article[cur.description[i][0]] = data[i]
            size += datasetgenerator.get_sample_count(article)
        cur.close()
        db.close()
        return size

    def train_tokenizer_on_articles(self, tokenizer, lang, start, end,randomizationseed=None, status="RAW"):
        db = self.database.conn()
        cur = db.cursor()
        cur.execute(Articles.get_query(lang, start, end, randomizationseed, status))
        for data in cur:
            article = {}
            for i in range(len(data)): article[cur.description[i][0]] = data[i]
            tokenizer.train_on_article(article)
        cur.close()
        db.close()