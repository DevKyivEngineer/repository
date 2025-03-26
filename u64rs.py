

from Person import Person

class FullTimeStudent(Person):
    def_init_(self,name,age,prac_score,prac_count,exam_scr,attend,pct):
    super()._inint_(name,age)
    self.prac_score = prac_score
    self.prac_count = prac_count
    self.exam_scr = exam_scr
    self.exam_attend_pct

    def avg_practice_score(self):
        if self.prac_count!=0:
            avg_prac = self.prac_score / self.prac_count
        else:
            avg_prac = 0
            return avg_prac

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        S_att = self.attend_pct
        return #додайте код по формулі

    student1 = FullTimeStudent(name="KOLA",age=24,prac_score=910,prac_count=10,exam_scr=95,attend_pct=85)
    student2 = FullTimeStudent("Klavdia Petrivna",19,930,10,99,20)

