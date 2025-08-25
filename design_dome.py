import numpy as np

# 1. numpy 임포트 (위에서 완료)

# 2. CSV 파일들을 읽어들여 부품명과 강도값을 함께 처리
try:
    # CSV 파일을 텍스트로 읽어서 처리
    def read_csv_data(filename):
        parts_data = []
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]  # 헤더 제외
            for line in lines:
                parts_name, strength = line.strip().split(',')
                parts_data.append((parts_name, int(strength)))
        return parts_data
    
    data1 = read_csv_data('mars_base_main_parts-001.csv')
    data2 = read_csv_data('mars_base_main_parts-002.csv')
    data3 = read_csv_data('mars_base_main_parts-003.csv')
    print('모든 CSV 파일을 성공적으로 로드했습니다.')
except FileNotFoundError as e:
    print(f'오류: 파일을 찾을 수 없습니다 - {e}')
    exit(1)
except Exception as e:
    print(f'CSV 파일 로드 오류: {e}')
    exit(1)

# 3. 3개의 데이터를 하나로 합치기
all_parts_data = data1 + data2 + data3
print(f'전체 부품 데이터 수: {len(all_parts_data)}')

# 4. 각 부품별 평균값 계산
parts_dict = {}
for parts_name, strength in all_parts_data:
    if parts_name not in parts_dict:
        parts_dict[parts_name] = []
    parts_dict[parts_name].append(strength)

# 각 부품의 평균 강도 계산
parts_averages = {}
for parts_name, strengths in parts_dict.items():
    parts_averages[parts_name] = np.mean(strengths)

print(f'고유 부품 종류 수: {len(parts_averages)}')

# parts 배열 생성 (평균값들로 구성)
parts = np.array(list(parts_averages.values()))
parts_names = list(parts_averages.keys())

# 5. 평균값이 50보다 작은 부품들을 뽑아내기
weak_parts_mask = parts < 50
weak_parts_strengths = parts[weak_parts_mask]
weak_parts_names = [parts_names[i] for i in range(len(parts_names)) if weak_parts_mask[i]]

# parts_to_work_on 배열 생성 (약한 부품들의 평균 강도)
parts_to_work_on = weak_parts_strengths

# 예외처리와 함께 CSV 파일로 저장
try:
    # 부품명과 평균 강도를 함께 저장
    with open('parts_to_work_on.csv', 'w') as file:
        file.write('parts,average_strength\n')
        for name, strength in zip(weak_parts_names, weak_parts_strengths):
            file.write(f'{name},{strength:.2f}\n')
    print(f'평균 강도 < 50인 {len(weak_parts_names)}개 부품을 parts_to_work_on.csv에 성공적으로 저장했습니다.')
except Exception as e:
    print(f'parts_to_work_on.csv 저장 오류: {e}')
    exit(1)

# 분석 결과 출력
print(f'\n분석 결과:')
print(f'전체 고유 부품 종류: {len(parts_averages)}')
print(f'보강이 필요한 부품 종류 (평균 강도 < 50): {len(weak_parts_names)}')
print(f'전체 부품의 평균 강도: {np.mean(parts):.2f}')
print(f'보강이 필요한 부품 비율: {(len(weak_parts_names) / len(parts_averages)) * 100:.1f}%')

print(f'\n보강이 필요한 부품 목록:')
for name, avg_strength in zip(weak_parts_names, weak_parts_strengths):
    print(f'  {name}: {avg_strength:.2f}')

print('\n화성 기지 취약점 분석이 성공적으로 완료되었습니다!')
