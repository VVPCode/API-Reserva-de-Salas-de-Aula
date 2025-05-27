from database import db
from datetime import date, time

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_turma = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'id_turma': self.id_turma,
            'sala': self.sala,
            'data_reserva': self.data_reserva.strftime('%Y-%m-%d'),
            'horario': self.horario.strftime('%H:%M')
        }
