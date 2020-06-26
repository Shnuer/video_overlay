import dir_command
import work_with_csv
import subtitle_preparation
import argparse

#!/usr/bin/env python3

def create_parser():
    parser = argparse.ArgumentParser(description='Overlay data from scv file to video. \n Example: \n main.py -i input_name.avi -d data.csv -o output_name.avi')
    parser.add_argument('-i', '--input', help="Specify the input file",nargs=1, type=str, required=True)
    parser.add_argument('-o', '--output', help="Specify the output file",nargs=1, type=str, required=True)
    parser.add_argument('-d', '--data', help="Specify the data file",nargs=1, type=str, required=True)
    parser.add_argument('-f', '--freq', help="Specify the data frequency in Hz",nargs=1, type=float, default=50.0)
    parser.add_argument('-s', '--subtitle', help="Specify the name subtitle file",nargs=1, type=str, default='file.ass')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = create_parser()

    START_TIME = 0

    input_video_file_name = args.input[0]
    data_file_name = args.data[0]
    output_video_file_name = args.output[0]
    step_size = 1 / args.freq
    file_name_subtitle = args.subtitle


    duration = dir_command.get_duration_video_in_seconds(input_video_file_name)

    title = work_with_csv.get_title_from_csv(data_file_name)
    data_gen = work_with_csv.get_data_from_csv(data_file_name)


    # Creating a subtitle file
    subtitle_preparation.create_subtitle_file(duration=duration, title=title, data_gen=data_gen,
                                                file_name_subtitle=file_name_subtitle, 
                                                start_time=START_TIME, 
                                                step_size=step_size)

    # Video captioning
    dir_command.overlay_sub_to_video(input_video_file_name=input_video_file_name, 
                                        output_video_file_name=output_video_file_name, 
                                        file_name_subtitle=file_name_subtitle)





