! Lab 4, task 2

program task2
    implicit none
    integer, parameter :: N=5, display_iteration = 1
    real(kind=8) :: odd_sum
    


    call computeSum(N,odd_sum,display_iteration)
    print *, 'odd_sum=',odd_sum


end program task2

!------------
!Subroutine which sums the first N odd integers
subroutine computeSum(N, odd_sum, display_iteration)
        implicit none
        integer, parameter :: N,
! To compile this code:
! $ gfortran -o task2.exe lab42soln.f90
! To run the resulting executable: $ ./task2.exe
