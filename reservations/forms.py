# import pandas as pd
from django.core.exceptions import ValidationError
from django.forms import (
    ModelForm,
    SelectDateWidget,
    Select,
    CheckboxSelectMultiple,
)
from django import forms
from django.utils.translation import gettext_lazy as _

from reservations.models import Reservations, TennisCourt

RENT_TIME = [
    ('8.00', '8.00'),
    ('8.30', '8.30'),
    ('9.00', '9.00'),
    ('9.30', '9.30'),
    ('10.00', '10.00'),
    ('10.30', '10.30'),
    ('11.00', '11.00'),
    ('11.30', '11.30'),
    ('12.00', '12.00'),
    ('12.30', '12.30'),
    ('13.00', '13.00'),
    ('13.30', '13.30'),
    ('14.00', '14.00'),
    ('14.30', '14.30'),
    ('15.00', '15.00'),
    ('15.30', '15.30'),
    ('16.30', '16.00'),
    ('17.00', '17.00'),
    ('17.30', '17.30'),
    ('18.00', '18.00'),
    ('18.30', '18.30'),
    ('19.00', '19.00'),
    ('19.30', '19.30'),
    ('20.00', '20.00'),
    ('20.30', '20.30'),
    ('21.00', '21.00'),
    ('21.30', '21.30'),
    ('22.00', '22.00'),
]
RENT_TIME_2 = [
    ('8:00', '8:00'),
    ('8:30', '8:30'),
    ('9:00', '9:00'),
    ('9:30', '9:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:30', '16:00'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19.00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
]


class CreateReservationModelForm(ModelForm):
    rez_start = Reservations.reservation_start
    rez_end = Reservations.reservation_end

    def clean(self):
        cleaned_data = super().clean()
        rez_start = cleaned_data.get('reservation_start')
        rez_end = cleaned_data.get('reservation_end')

        if rez_end < rez_start:
            raise ValidationError(f'WARNING!!! Reservation end time you have chosen is lower than '
                                  f'start of your reservation. Change reservation finish time.')
        if rez_end == rez_start:
            raise ValidationError(f'WARNING!!! Reservation start and end time are the same. '
                                  f' Change reservation time.')
        return cleaned_data

    class Meta:
        model = Reservations
        fields = [
            'court',
            'reservation_date',
            'reservation_start',
            'reservation_end',
        ]
        widgets = {
            'reservation_date': SelectDateWidget(
                empty_label=("Choose Day", "Choose Month", "Choose Year")),
            'reservation_start': forms.Select(choices=RENT_TIME),
            'reservation_end': Select(choices=RENT_TIME),
        }

        help_texts = {'reservation_start': _('( hh.mm )'),
                      'reservation_end': _('( hh.mm )'),
                      }


class CreateReservationWithSelectedCourtForm(ModelForm):
    rez_start = Reservations.reservation_start
    rez_end = Reservations.reservation_end

    def clean(self):
        cleaned_data = super().clean()
        rez_start = cleaned_data.get('reservation_start')
        rez_end = cleaned_data.get('reservation_end')

        if rez_end < rez_start:
            raise ValidationError(f'WARNING!!! '
                                  f'Reservation end time you have chosen is before your reservation '
                                  f'starts. Change reservation start or end time.')
        if rez_end == rez_start:
            raise ValidationError(f'WARNING!!! Reservation start and end time are the same. '
                                  f' Change reservation start or end time.')
        return cleaned_data

    class Meta:
        model = Reservations
        fields = [
            'reservation_date',
            'reservation_start',
            'reservation_end',
        ]
        widgets = {
            'reservation_date': SelectDateWidget(
                empty_label=("Choose Day", "Choose Month", "Choose Year")),
            'reservation_start': forms.Select(choices=RENT_TIME),
            'reservation_end': Select(choices=RENT_TIME),
        }

        help_texts = {'reservation_start': _('( hh.mm )'),
                      'reservation_end': _('( hh.mm )'),
                      }


class CreateExactReservationModelForm(forms.Form):
    reservation_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Day", "Choose Month", "Choose Year")))
    # datelist = pd.date_range(start=TennisCourt.open_hour, end=TennisCourt.close_hour,
    #                          freq='0.5H').to_pydatetime().tolist()
    # renting_time = []
    # for hours in datelist:
    #     hour = str(hours)[11:16]
    #     renting_time.append((hour, hour))
    # k =[
    #  (str(TennisCourt.open_hour), TennisCourt.open_hour),
    #   (TennisCourt.close_hour, TennisCourt.close_hour),
    # ]

    reservation_start = forms.ChoiceField(help_text='( hh.mm )', choices=RENT_TIME_2)
    # reservation_start = forms.ChoiceField(choices=RENT_TIME)
    reservation_end = forms.ChoiceField(help_text='( hh.mm )', choices=RENT_TIME_2)
    #
    # help_texts = {'reservation_start': _('( hh.mm )'),
    #               'reservation_end': _('( hh.mm )'),
    #               }


class AddCourtModelForm(ModelForm):
    class Meta:
        model = TennisCourt
        # fields = '__all__'
        exclude = ['reservation_status']
        widgets = {
            'open_hour': forms.Select(choices=RENT_TIME),
            'close_hour': Select(choices=RENT_TIME),
        }

        help_texts = {'open_hour': '( hh.mm )',
                      'close_hour': '( hh.mm )',
                      }


class DeleteCourtForm(ModelForm):
    class Meta:
        model = Reservations
        fields = ['court']
        widgets = {
            'court': CheckboxSelectMultiple
        }


class CourtsParamsEditForm(ModelForm):
    class Meta:
        model = TennisCourt
        # fields = '__all__'
        exclude = ['reservation_status']
        widgets = {
            'open_hour': forms.Select(choices=RENT_TIME),
            'close_hour': Select(choices=RENT_TIME),
        }

        help_texts = {'open_hour': _('( hh.mm )'),
                      'close_hour': _('( hh.mm )'),
                      }


class ReservationsParamsEditForm(ModelForm):
    class Meta:
        model = Reservations
        fields = [
            'court',
            'reservation_date',
            'reservation_start',
            'reservation_end',
        ]
        widgets = {
            'reservation_date': SelectDateWidget(
                empty_label=("Choose Day", "Choose Month", "Choose Year")),
            'reservation_start': forms.Select(choices=RENT_TIME),
            'reservation_end': Select(choices=RENT_TIME),
        }

        help_texts = {'reservation_start': _('( hh.mm )'),
                      'reservation_end': _('( hh.mm )'),
                      }


if __name__ == '__main__':
    pass
