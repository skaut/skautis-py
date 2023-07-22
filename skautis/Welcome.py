# -*- coding: utf-8 -*-

import zeep

# Uvítací balíčky
class Welcome(object):
    __module__ = 'skautis'

    def __init__(self, test):
        if test:
            self._client = zeep.Client('https://test-is.skaut.cz/JunakWebservice/Welcome.asmx?wsdl')
        else:
            self._client = zeep.Client('https://is.skaut.cz/JunakWebservice/Welcome.asmx?wsdl')

    # Načíst seznam vazeb funkcí a uvítacího balíčku
    def WelcomeFunctionAll(self, ID_Login, ID_Welcome, ID, ID_FunctionType):
        return self._client.service.WelcomeFunctionAll({"ID_Login": ID_Login, "ID_Welcome": ID_Welcome, "ID": ID, "ID_FunctionType": ID_FunctionType})

    # Smazat vazbu funkce a uvítacího balíčku
    def WelcomeFunctionDelete(self, ID_Login, ID):
        return self._client.service.WelcomeFunctionDelete({"ID_Login": ID_Login, "ID": ID})

    # Založit vazbu funkce a uvítacího balíčku
    def WelcomeFunctionInsert(self, ID_Login, ID, ID_Welcome, ID_FunctionType, Welcome=None, FunctionType=None):
        return self._client.service.WelcomeFunctionInsert({"ID_Login": ID_Login, "ID": ID, "ID_Welcome": ID_Welcome, "ID_FunctionType": ID_FunctionType, "Welcome": Welcome, "FunctionType": FunctionType})

    # Odeslat balíček k otestování
    def WelcomeMessage(self, ID_Login, ID, ID_Person, ID_FunctionType):
        return self._client.service.WelcomeMessage({"ID_Login": ID_Login, "ID": ID, "ID_Person": ID_Person, "ID_FunctionType": ID_FunctionType})

    # Odeslat balíček
    def WelcomeSentInsert(self, ID_Login, ID_Function, ID_Welcome):
        return self._client.service.WelcomeSentInsert({"ID_Login": ID_Login, "ID_Function": ID_Function, "ID_Welcome": ID_Welcome})

    # Odeslání balíčků
    def WelcomeSentUpdateSend(self, ID_Login):
        return self._client.service.WelcomeSentUpdateSend({"ID_Login": ID_Login})

    # Odeslat balíček všem v dané funkci
    def WelcomeUpdateSend(self, ID_Login, ID):
        return self._client.service.WelcomeUpdateSend({"ID_Login": ID_Login, "ID": ID})

    # Upravit uvítací balíček
    def WelcomeUpdate(self, ID_Login, ID, IsEnabled, IsParentUnit, IsSupervisorSent, SendToAll, IsFinal, DisplayName=None, Functions=None):
        return self._client.service.WelcomeUpdate({"ID_Login": ID_Login, "ID": ID, "IsEnabled": IsEnabled, "IsParentUnit": IsParentUnit, "IsSupervisorSent": IsSupervisorSent, "SendToAll": SendToAll, "IsFinal": IsFinal, "DisplayName": DisplayName, "Functions": Functions})

    # Načíst seznam pruhů balíčku
    def StripeAll(self, ID_Login, ID_Welcome, ID_AlignmentType, DisplayName=None, ID_Sex=None):
        return self._client.service.StripeAll({"ID_Login": ID_Login, "ID_Welcome": ID_Welcome, "ID_AlignmentType": ID_AlignmentType, "DisplayName": DisplayName, "ID_Sex": ID_Sex})

    # Načíst seznam příloh pruhu
    def StripeAttachmentAll(self, ID_Login, ID_Stripe, IsHtmlImage, DisplayName=None):
        return self._client.service.StripeAttachmentAll({"ID_Login": ID_Login, "ID_Stripe": ID_Stripe, "IsHtmlImage": IsHtmlImage, "DisplayName": DisplayName})

    # Smazat přílohu pruhu
    def StripeAttachmentDelete(self, ID_Login, ID):
        return self._client.service.StripeAttachmentDelete({"ID_Login": ID_Login, "ID": ID})

    # Stáhne přílohu pruhu
    def StripeAttachmentDownload(self, ID_Login, ID):
        return self._client.service.StripeAttachmentDownload({"ID_Login": ID_Login, "ID": ID})

    # Založit přílohu pruhu
    def StripeAttachmentInsert(self, ID_Login, ID, ID_Stripe, IsHtmlImage, DisplayName=None, Extension=None, Content=None):
        return self._client.service.StripeAttachmentInsert({"ID_Login": ID_Login, "ID": ID, "ID_Stripe": ID_Stripe, "IsHtmlImage": IsHtmlImage, "DisplayName": DisplayName, "Extension": Extension, "Content": Content})

    # Upravit přílohu pruhu
    def StripeAttachmentUpdate(self, ID_Login, ID, ID_Stripe, IsHtmlImage, DisplayName=None, Extension=None, Content=None):
        return self._client.service.StripeAttachmentUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Stripe": ID_Stripe, "IsHtmlImage": IsHtmlImage, "DisplayName": DisplayName, "Extension": Extension, "Content": Content})

    # Smazat pruh balíčku
    def StripeDelete(self, ID_Login, ID):
        return self._client.service.StripeDelete({"ID_Login": ID_Login, "ID": ID})

    # Načíst detail pruhu balíčku
    def StripeDetail(self, ID_Login, ID):
        return self._client.service.StripeDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit pruh balíčku
    def StripeInsert(self, ID_Login, ID, ID_Welcome, Order, IsNew, ID_AlignmentType, IsWarning, Welcome=None, DisplayName=None, Text=None, ID_Sex=None, Sex=None, AlignmentType=None):
        return self._client.service.StripeInsert({"ID_Login": ID_Login, "ID": ID, "ID_Welcome": ID_Welcome, "Order": Order, "IsNew": IsNew, "ID_AlignmentType": ID_AlignmentType, "IsWarning": IsWarning, "Welcome": Welcome, "DisplayName": DisplayName, "Text": Text, "ID_Sex": ID_Sex, "Sex": Sex, "AlignmentType": AlignmentType})

    # Upravit pruh balíčku
    def StripeUpdate(self, ID_Login, ID, ID_Welcome, Order, IsNew, ID_AlignmentType, IsWarning, Welcome=None, DisplayName=None, Text=None, ID_Sex=None, Sex=None, AlignmentType=None):
        return self._client.service.StripeUpdate({"ID_Login": ID_Login, "ID": ID, "ID_Welcome": ID_Welcome, "Order": Order, "IsNew": IsNew, "ID_AlignmentType": ID_AlignmentType, "IsWarning": IsWarning, "Welcome": Welcome, "DisplayName": DisplayName, "Text": Text, "ID_Sex": ID_Sex, "Sex": Sex, "AlignmentType": AlignmentType})

    # Načíst seznam uvítacích balíčků
    def WelcomeAll(self, ID_Login, ID_FunctionType, SendToAll, IsEnabled, DisplayName=None, ID_UnitType=None):
        return self._client.service.WelcomeAll({"ID_Login": ID_Login, "ID_FunctionType": ID_FunctionType, "SendToAll": SendToAll, "IsEnabled": IsEnabled, "DisplayName": DisplayName, "ID_UnitType": ID_UnitType})

    # Načíst detail uvítacího balíčku
    def WelcomeDetail(self, ID_Login, ID):
        return self._client.service.WelcomeDetail({"ID_Login": ID_Login, "ID": ID})

    # Založit uvítací balíček
    def WelcomeInsert(self, ID_Login, IsEnabled, IsParentUnit, IsFinal, Functions=None, DisplayName=None):
        return self._client.service.WelcomeInsert({"ID_Login": ID_Login, "IsEnabled": IsEnabled, "IsParentUnit": IsParentUnit, "IsFinal": IsFinal, "Functions": Functions, "DisplayName": DisplayName})

    # Načíst seznam odeslání balíčků
    def WelcomeSentAll(self, ID_Login, ID_Unit, ID_Welcome):
        return self._client.service.WelcomeSentAll({"ID_Login": ID_Login, "ID_Unit": ID_Unit, "ID_Welcome": ID_Welcome})

    # Upravit odeslání balíčku
    def WelcomeSentUpdate(self, ID_Login, ID):
        return self._client.service.WelcomeSentUpdate({"ID_Login": ID_Login, "ID": ID})

    # Připravit balíček k odeslání všem v dané funkci
    def WelcomeUpdatePrepareSend(self, ID_Login, ID):
        return self._client.service.WelcomeUpdatePrepareSend({"ID_Login": ID_Login, "ID": ID})

    # Načíst seznam proměnných balíčku
    def WelcomeVariableAll(self, ID_Login, DisplayName=None):
        return self._client.service.WelcomeVariableAll({"ID_Login": ID_Login, "DisplayName": DisplayName})

