from rest_framework import serializers

class SalarySerializer(serializers.Serializer):
    vacation_days = serializers.IntegerField()
    working_days = serializers.IntegerField(max_value=31)
    holiday_days = serializers.IntegerField(validators=[self.validate_holiday_days])

    def validate_vacation_days(self, value):
        if value > 5:
            raise serializers.ValidationError("The number of vacation days cannot exceed 5.")
        return value

    def validate_holiday_days(self, value):
        if value > 10:
            raise serializers.ValidationError("The number of holiday days cannot exceed 10.")
        return value
