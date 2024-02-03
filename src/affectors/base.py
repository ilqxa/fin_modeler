from abc import ABC, abstractclassmethod
from datetime import date


class Affector(ABC):
	@abstractclassmethod
	def get_day_result(self, day: int) -> float:
		...


class RegularJob(Affector):
	def __init__(
		self,
		salary: float,
		advancePaymentDay: date,
		mainPaymentDay: int,
	) -> None:
		self.salary = salary
		self.advancePaymentDay = advancePaymentDay
		self.mainPaymentDay = mainPaymentDay
	
	def get_day_result(self, day: int) -> float:
		return 1.
