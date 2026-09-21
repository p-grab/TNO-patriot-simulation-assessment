from radar import Radar


def test_radar_sequential_reads(tmp_path):
    file_path = tmp_path / "radar.csv"
    file_path.write_text(
        "0000001;0000010;0000011\n"
        "0000100;0000101;0000110\n"
    )

    radar = Radar(file_path)

    first_scan = radar.scan()
    second_scan = radar.scan()

    radar.close_file()

    assert first_scan == ["0000001", "0000010", "0000011"]
    assert second_scan == ["0000100", "0000101", "0000110"]


def test_radar_eof_returns_none(tmp_path):
    file_path = tmp_path / "radar.csv"
    file_path.write_text("0000001;0000010\n")

    radar = Radar(file_path)

    radar.scan()
    result = radar.scan()

    radar.close_file()

    assert result is None


def test_radar_empty_file_returns_none(tmp_path):
    file_path = tmp_path / "radar.csv"
    file_path.write_text("")

    radar = Radar(file_path)

    result = radar.scan()

    radar.close_file()

    assert result is None