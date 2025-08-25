import numpy as np

# 1. numpy 임포트 (위에서 완료)

# 2. CSV 파일들을 numpy를 사용해서 읽어들여 ndarray로 생성
try:
    arr1 = np.loadtxt('mars_base_main_parts-001.csv', delimiter=',', skiprows=1)
    arr2 = np.loadtxt('mars_base_main_parts-002.csv', delimiter=',', skiprows=1)
    arr3 = np.loadtxt('mars_base_main_parts-003.csv', delimiter=',', skiprows=1)
    print('모든 CSV 파일을 성공적으로 로드했습니다.')
except FileNotFoundError as e:
    print(f'오류: 파일을 찾을 수 없습니다 - {e}')
    exit(1)
except Exception as e:
    print(f'CSV 파일 로드 오류: {e}')
    exit(1)

# 3. 3개의 배열을 하나로 합치고 parts라는 ndarray 생성
parts = np.concatenate((arr1, arr2, arr3), axis=0)
print(f'병합된 배열의 크기: {parts.shape}')

# 4. parts를 이용해서 각 항목의 평균값 구하기
mean_values = np.mean(parts, axis=1)
print(f'평균값 계산 완료, 크기: {mean_values.shape}')

# 5. 평균값이 50보다 작은 값을 뽑아내서 parts_to_work_on.csv로 저장
parts_below_50_mask = mean_values < 50
parts_to_work_on = parts[parts_below_50_mask]

# 예외처리와 함께 CSV 파일로 저장
try:
    np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',', fmt='%.6f')
    print(f'평균 < 50인 {parts_to_work_on.shape[0]}개 부품을 parts_to_work_on.csv에 성공적으로 저장했습니다.')
except Exception as e:
    print(f'parts_to_work_on.csv 저장 오류: {e}')
    exit(1)

# 분석 결과 출력
print(f'\n분석 결과:')
print(f'전체 분석된 부품 수: {parts.shape[0]}')
print(f'보강이 필요한 부품 수 (평균 < 50): {parts_to_work_on.shape[0]}')
print(f'전체 부품의 평균 강도: {np.mean(parts):.2f}')
print(f'보강이 필요한 부품 비율: {(parts_to_work_on.shape[0] / parts.shape[0]) * 100:.1f}%')

print('\n화성 기지 취약점 분석이 성공적으로 완료되었습니다!')
