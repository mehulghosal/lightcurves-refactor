import numpy as np

def convert_ps1_g_to_sdss_g(ps1_g, ps1_g_err, ps1_g_minus_r, ps1_g_minus_r_error):
    B_0, B_1, B_err = -0.012, -0.139, 0.007
    x = ps1_g_minus_r
    y = B_0 + (B_1*x)
    g_sdss_minus_g_ps1 = y
    g_sdss = g_sdss_minus_g_ps1 + ps1_g
    #errors
    #B_1 * x error
    first_step_product_error = (ps1_g_minus_r * B_1) * np.sqrt((ps1_g_minus_r_error/ps1_g_minus_r)**2 + (B_err/B_1)**2)
    second_step_sum_error = np.sqrt(B_err**2 + first_step_product_error**2)
    third_step_subtraction_error = np.sqrt(second_step_sum_error**2 + (ps1_g_err**2))
    return g_sdss, third_step_subtraction_error


def convert_ps1_r_to_sdss_r(ps1_g, ps1_g_err, ps1_g_minus_r, ps1_g_minus_r_error):
    B_0, B_1, B_err = 0.0, -0.007, 0.002
    x = ps1_g_minus_r
    y = B_0 + (B_1*x)
    g_sdss_minus_g_ps1 = y
    g_sdss = g_sdss_minus_g_ps1 + ps1_g
    #errors
    #B_1 * x error
    first_step_product_error = (ps1_g_minus_r * B_1) * np.sqrt((ps1_g_minus_r_error/ps1_g_minus_r)**2 + (B_err/B_1)**2)
    second_step_sum_error = np.sqrt(B_err**2 + first_step_product_error**2)
    third_step_subtraction_error = np.sqrt(second_step_sum_error**2 + (ps1_g_err**2))
    return g_sdss, third_step_subtraction_error

def convert_ps1_i_to_sdss_i(ps1_g, ps1_g_err, ps1_g_minus_r, ps1_g_minus_r_error):
    B_0, B_1, B_err = 0.004, -0.014, 0.003
    x = ps1_g_minus_r
    y = B_0 + (B_1*x)
    g_sdss_minus_g_ps1 = y
    g_sdss = g_sdss_minus_g_ps1 + ps1_g
    #errors
    #B_1 * x error
    first_step_product_error = (ps1_g_minus_r * B_1) * np.sqrt((ps1_g_minus_r_error/ps1_g_minus_r)**2 + (B_err/B_1)**2)
    second_step_sum_error = np.sqrt(B_err**2 + first_step_product_error**2)
    third_step_subtraction_error = np.sqrt(second_step_sum_error**2 + (ps1_g_err**2))
    return g_sdss, third_step_subtraction_error
