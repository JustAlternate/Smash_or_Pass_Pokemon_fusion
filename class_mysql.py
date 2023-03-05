import mysql.connector
# Add in the database.
def connexion():
    connexion_mysql = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="smash_or_pass",
            password="smash_or_pass_passwd",
            database="Smash_or_Pass")
    return connexion_mysql

class mySqlAccount():
    def __init__(self):
        self.req = ""

    def commit(self):
        connexion_mysql = connexion()
        cur_BD = connexion_mysql.cursor()
        cur_BD.execute(self.req)
        connexion_mysql.commit()
        connexion_mysql.close()

    def fetch(self):
        connexion_mysql = connexion()
        cur_BD = connexion_mysql.cursor()
        cur_BD.execute(self.req)
        res = cur_BD.fetchall()
        connexion_mysql.close()
        return res

    def loadlisteAccount(self):
        self.req = "SELECT Fusion FROM fusion_scores;"
        self.listAccounts = self.fetch()

    def find_leaderboard(self):
        self.req = "SELECT Fusion,nbr_times_smashed,nbr_times_passed,timestamp FROM fusion_scores ORDER BY nbr_times_smashed DESC, timestamp ASC;"
        return self.fetch()

    def isindatabase(self, fusion_name):
        self.loadlisteAccount()
        for fusion in self.listAccounts:
            if fusion[0] == fusion_name:
                return True
        return False

    def maj_account(self, fusion, smashed, passed):
        if not self.isindatabase(fusion):
            self.req = "INSERT INTO fusion_scores VALUES ('" + str(fusion) + "','" + str(smashed) + "','" + str(passed) + "',CURRENT_TIMESTAMP());"
            self.commit()
        else:
            if smashed:
                self.req = "UPDATE fusion_scores SET nbr_times_smashed = nbr_times_smashed + 1, timestamp = CURRENT_TIMESTAMP() WHERE Fusion = '" + str(fusion) + "';"
            else:
                self.req = "UPDATE fusion_scores SET nbr_times_passed = nbr_times_passed + 1, timestamp = CURRENT_TIMESTAMP() WHERE Fusion = '" + str(fusion) + "';"
            self.commit()
