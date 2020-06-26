import dir_command
import work_with_csv
import subtitle_preparation
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description='Overlay data from scv file to video. \n Example: \n main.py -i input_name.avi -d data.csv -o output_name.avi')
    parser.add_argument('-i', '--input', help="Specify the input file",nargs=1, type=str, required=True)
    parser.add_argument('-o', '--output', help="Specify the output file",nargs=1, type=str, required=True)
    parser.add_argument('-d', '--data', help="Specify the data file",nargs=1, type=str, required=True)
    parser.add_argument('-f', '--freq', help="Specify the data frequency in Hz",nargs=1, type=float, default=50.0)
    parser.add_argument('-s', '--subtitle', help="Specify the name subtitle file",nargs=1, type=str, default='file')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = create_parser()

    INPUT_VIDEO_FILE_NAME = args.input[0]
    DATA_FILE_NAME = args.data[0]
    OUTPUT_VIDEO_FILE_NAME = args.output[0]
    STEP_SIZE = 1 / args.freq
    START_TIME = 0
    FILE_NAME_SUBTITLE = args.subtitle

    duration = dir_command.get_duration_video_in_seconds(INPUT_VIDEO_FILE_NAME)

    title = work_with_csv.get_title_from_csv(DATA_FILE_NAME)
    data_gen = work_with_csv.get_data_from_csv(DATA_FILE_NAME)


    # Creating a subtitle file
    subtitle_preparation.create_subtitle_file(duration=duration, title=title, data_gen=data_gen,
                                                file_name_subtitle=FILE_NAME_SUBTITLE, 
                                                start_time=START_TIME, 
                                                step_size=STEP_SIZE)

    # Video captioning
    dir_command.overlay_sub_to_video(input_video_file_name=INPUT_VIDEO_FILE_NAME, 
                                        output_video_file_name=OUTPUT_VIDEO_FILE_NAME, 
                                        file_name_subtitle=FILE_NAME_SUBTITLE)





