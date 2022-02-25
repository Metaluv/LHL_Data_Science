def equal_slices(total_slices, no_recipients, slices_each):
    return True if no_recipients * slices_each <= total_slices else False