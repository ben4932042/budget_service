from src.app import *


def test_get_illgal_input(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202111': 3000}
    )
    service = BudgetService()
    assert service.query( '20211102', '20211101' ) == float( 0 )


def test_get_full_one_month_budget(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202111': 3000}
    )
    service = BudgetService()
    assert service.query( '20211101', '20211130' ) == float( 3000 )


def test_get_partical_one_month_budget(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202111': 3000}
    )
    service = BudgetService()
    assert service.query( '20211101', '20211102' ) == float( 200 )


def test_get_partical_one_month_budget_without_data(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={}
    )
    service = BudgetService()
    assert service.query( '20211101', '20211102' ) == float( 0 )


def test_get_two_month_budget(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202111': 3000, '202112': 3100}
    )
    service = BudgetService()
    assert service.query( '20211101', '20211231' ) == float( 6100 )


def test_get_partical_two_month_budget(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202111': 3000, '202112': 3100}
    )
    service = BudgetService()
    assert service.query( '20211101', '20211210' ) == float( 4000 )


def test_get_partical_two_month_budget_without_data(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202111': 3000}
    )
    service = BudgetService()
    assert service.query( '20211101', '20211210' ) == float( 3000 )


def test_get_three_month_budget(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202110': 3100, '202111': 3000, '202112': 3100}
    )
    service = BudgetService()
    assert service.query( '20211001', '20211231' ) == float( 9200 )


def test_get_partical_three_month_budget(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202110': 3100, '202111': 3000, '202112': 3100}
    )
    service = BudgetService()
    assert service.query( '20211031', '20211231' ) == float( 6200 )

def test_get_partical_three_month_budget_without_data(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202110': 3100, '202112': 3100}
    )
    service = BudgetService()
    assert service.query( '20211031', '20211230' ) == float( 3100 )


def test_get_partical_three_month_budget_reverse_data(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202112': 3100, '202110': 3100, '202111': 0}
    )
    service = BudgetService()
    assert service.query( '20211031', '20211231' ) == float( 3200 )


def test_get_partical_three_month_budget_with_zero_data(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202110': 3100, '202111': 0, '202112': 3100}
    )
    service = BudgetService()
    assert service.query( '20211031', '20211231' ) == float( 3200 )


def test_get_budget_over_year(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202112': 3100, '202201': 6200}
    )
    service = BudgetService()
    assert service.query( '20211201', '20220131' ) == float( 9300 )

def test_get_partical_budget_over_year(mocker):
    mocker.patch(
        'src.app.BudgetRepo.get_all',
        return_value={'202112': 3100, '202201': 6200}
    )
    service = BudgetService()
    assert service.query( '20211201', '20220130' ) == float( 9100 )