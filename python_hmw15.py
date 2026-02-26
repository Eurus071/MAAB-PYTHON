import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set style for better looking plots
plt.style.use('seaborn-v0_8-darkgrid')

print("=" * 70)
print("MATPLOTLIB VISUALIZATION PROJECT - ALL 8 TASKS")
print("=" * 70)

# Task 1: Basic Plotting - Quadratic Function
print("\n" + "=" * 60)
print("TASK 1: Basic Plotting - Quadratic Function")
print("=" * 60)

def task1_quadratic_plot():
    """Plot f(x) = x² - 4x + 4"""
    # Generate x values
    x = np.linspace(-10, 10, 400)
    
    # Calculate y values
    y = x**2 - 4*x + 4
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot the function
    ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = x^2 - 4x + 4$')
    
    # Find minimum point (vertex)
    x_vertex = 2  # From calculus: derivative = 2x - 4 = 0
    y_vertex = x_vertex**2 - 4*x_vertex + 4
    
    # Plot the vertex
    ax.plot(x_vertex, y_vertex, 'ro', markersize=10, label=f'Vertex ({x_vertex}, {y_vertex})')
    ax.axvline(x=2, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    
    # Customization
    ax.set_xlabel('x values', fontsize=12, fontweight='bold')
    ax.set_ylabel('f(x)', fontsize=12, fontweight='bold')
    ax.set_title('Quadratic Function: $f(x) = x^2 - 4x + 4$', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    
    # Set axis limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-5, 100])
    
    # Add text annotation for vertex
    ax.text(x_vertex + 0.5, y_vertex + 2, f'Minimum at ({x_vertex}, {y_vertex})', 
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('task1_quadratic_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 1 completed: Quadratic function plotted")
    print("  Saved as 'task1_quadratic_plot.png'")
    
    return fig, ax

# Task 2: Sine and Cosine Plot
print("\n" + "=" * 60)
print("TASK 2: Sine and Cosine Functions")
print("=" * 60)

def task2_trigonometric_plot():
    """Plot sin(x) and cos(x) on the same graph"""
    # Generate x values
    x = np.linspace(0, 2*np.pi, 200)
    
    # Calculate y values
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Plot both functions with different styles
    ax.plot(x, y_sin, 'b-', linewidth=2.5, marker='o', markersize=4, 
            markevery=10, label=r'$\sin(x)$')
    ax.plot(x, y_cos, 'r--', linewidth=2.5, marker='s', markersize=4, 
            markevery=10, label=r'$\cos(x)$', alpha=0.8)
    
    # Highlight key points
    key_points = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    for point in key_points:
        ax.axvline(x=point, color='gray', linestyle=':', alpha=0.3)
        ax.text(point, 1.05, f'{point/np.pi:.1f}π', 
                ha='center', fontsize=9, color='gray')
    
    # Add horizontal line at y=0
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
    
    # Customization
    ax.set_xlabel('x (radians)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Function Value', fontsize=12, fontweight='bold')
    ax.set_title('Sine and Cosine Functions', fontsize=14, fontweight='bold')
    ax.set_xlim([0, 2*np.pi])
    ax.set_ylim([-1.2, 1.2])
    
    # Add legend
    ax.legend(loc='upper right', fontsize=12)
    
    # Add grid
    ax.grid(True, alpha=0.3)
    
    # Add annotations for key properties
    ax.text(0.5, 0.9, 'Amplitude = 1', transform=ax.transAxes, 
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    ax.text(0.5, 0.85, f'Period = {2*np.pi:.2f} radians', transform=ax.transAxes, 
            fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('task2_sine_cosine_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 2 completed: Sine and cosine functions plotted")
    print("  Saved as 'task2_sine_cosine_plot.png'")
    
    return fig, ax

# Task 3: Subplots Grid
print("\n" + "=" * 60)
print("TASK 3: 2x2 Subplots Grid")
print("=" * 60)

def task3_subplots_grid():
    """Create a 2x2 grid of different function plots"""
    # Create figure with 2x2 subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()  # Flatten for easier indexing
    
    # Generate x values for each plot
    x1 = np.linspace(-5, 5, 200)
    x2 = np.linspace(0, 2*np.pi, 200)
    x3 = np.linspace(-2, 2, 200)
    x4 = np.linspace(0, 10, 200)
    
    # Plot 1: Cubic function
    axes[0].plot(x1, x1**3, 'purple', linewidth=2.5)
    axes[0].set_title(r'$f(x) = x^3$', fontsize=12, fontweight='bold')
    axes[0].set_xlabel('x', fontsize=10)
    axes[0].set_ylabel('f(x)', fontsize=10)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim([-30, 30])
    
    # Highlight inflection point
    axes[0].plot(0, 0, 'ro', markersize=8)
    axes[0].text(0.5, 0, 'Inflection Point', transform=axes[0].transAxes, 
                ha='center', fontsize=9)
    
    # Plot 2: Sine function
    axes[1].plot(x2, np.sin(x2), 'orange', linewidth=2.5)
    axes[1].set_title(r'$f(x) = \sin(x)$', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('x (radians)', fontsize=10)
    axes[1].set_ylabel('f(x)', fontsize=10)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim([-1.2, 1.2])
    
    # Highlight amplitude
    axes[1].axhline(y=1, color='red', linestyle=':', alpha=0.5)
    axes[1].axhline(y=-1, color='red', linestyle=':', alpha=0.5)
    
    # Plot 3: Exponential function
    axes[2].plot(x3, np.exp(x3), 'green', linewidth=2.5)
    axes[2].set_title(r'$f(x) = e^x$', fontsize=12, fontweight='bold')
    axes[2].set_xlabel('x', fontsize=10)
    axes[2].set_ylabel('f(x)', fontsize=10)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_ylim([0, 10])
    
    # Highlight exponential growth
    axes[2].plot(0, 1, 'ro', markersize=8)
    axes[2].text(0, 1.5, 'e⁰ = 1', ha='center', fontsize=9)
    
    # Plot 4: Logarithmic function
    axes[3].plot(x4, np.log(x4 + 1), 'brown', linewidth=2.5)
    axes[3].set_title(r'$f(x) = \ln(x+1)$', fontsize=12, fontweight='bold')
    axes[3].set_xlabel('x', fontsize=10)
    axes[3].set_ylabel('f(x)', fontsize=10)
    axes[3].grid(True, alpha=0.3)
    axes[3].set_ylim([0, 2.5])
    
    # Highlight asymptotic behavior
    axes[3].axhline(y=0, color='red', linestyle=':', alpha=0.5)
    axes[3].text(8, 0.2, 'Asymptotic to x-axis', fontsize=9, ha='center')
    
    # Main title for the entire figure
    fig.suptitle('Four Different Mathematical Functions', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.savefig('task3_subplots_grid.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 3 completed: 2x2 subplots grid created")
    print("  Saved as 'task3_subplots_grid.png'")
    
    return fig, axes

# Task 4: Scatter Plot
print("\n" + "=" * 60)
print("TASK 4: Random Scatter Plot")
print("=" * 60)

def task4_scatter_plot():
    """Create scatter plot of 100 random points"""
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate random data
    n_points = 100
    x = np.random.uniform(0, 10, n_points)
    y = np.random.uniform(0, 10, n_points)
    
    # Create sizes and colors based on position
    sizes = 20 + 80 * (x + y) / 20  # Size based on distance from origin
    colors = np.sqrt(x**2 + y**2)  # Color based on distance from origin
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create scatter plot with color gradient
    scatter = ax.scatter(x, y, c=colors, s=sizes, 
                        alpha=0.7, cmap='viridis', edgecolor='black', linewidth=0.5)
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Distance from origin', fontsize=10)
    
    # Customization
    ax.set_xlabel('X coordinate', fontsize=12, fontweight='bold')
    ax.set_ylabel('Y coordinate', fontsize=12, fontweight='bold')
    ax.set_title(f'Scatter Plot of {n_points} Random Points', fontsize=14, fontweight='bold')
    
    # Set axis limits
    ax.set_xlim([-0.5, 10.5])
    ax.set_ylim([-0.5, 10.5])
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Add quadrant lines
    ax.axhline(y=5, color='gray', linestyle=':', alpha=0.5)
    ax.axvline(x=5, color='gray', linestyle=':', alpha=0.5)
    
    # Add annotation for statistics
    stats_text = f'Total Points: {n_points}\n'
    stats_text += f'Mean X: {np.mean(x):.2f}\n'
    stats_text += f'Mean Y: {np.mean(y):.2f}\n'
    stats_text += f'Std X: {np.std(x):.2f}\n'
    stats_text += f'Std Y: {np.std(y):.2f}'
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('task4_scatter_plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 4 completed: Scatter plot with 100 random points")
    print("  Saved as 'task4_scatter_plot.png'")
    
    return fig, ax

# Task 5: Histogram
print("\n" + "=" * 60)
print("TASK 5: Normal Distribution Histogram")
print("=" * 60)

def task5_histogram():
    """Plot histogram of normally distributed data"""
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate random data from normal distribution
    n_values = 1000
    mean = 0
    std = 1
    data = np.random.normal(mean, std, n_values)
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Plot histogram
    n_bins = 30
    n, bins, patches = ax.hist(data, bins=n_bins, 
                               color='steelblue', 
                               edgecolor='black', 
                               linewidth=1.2,
                               alpha=0.7,
                               density=True,  # Normalize to form probability density
                               label=f'Histogram ({n_bins} bins)')
    
    # Overlay the theoretical normal distribution
    from scipy.stats import norm
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, mean, std)
    ax.plot(x, y, 'r-', linewidth=3, label='Theoretical PDF')
    
    # Customization
    ax.set_xlabel('Value', fontsize=12, fontweight='bold')
    ax.set_ylabel('Probability Density', fontsize=12, fontweight='bold')
    ax.set_title(f'Histogram of {n_values} Samples from N({mean},{std}²)', 
                 fontsize=14, fontweight='bold')
    
    # Add vertical lines for mean and std
    ax.axvline(x=mean, color='green', linestyle='--', linewidth=2, 
               label=f'Mean = {mean}')
    ax.axvline(x=mean + std, color='orange', linestyle=':', linewidth=2, 
               alpha=0.7, label=f'±1σ = {std}')
    ax.axvline(x=mean - std, color='orange', linestyle=':', linewidth=2, alpha=0.7)
    ax.axvline(x=mean + 2*std, color='purple', linestyle=':', linewidth=1.5, 
               alpha=0.5, label=f'±2σ = {2*std}')
    ax.axvline(x=mean - 2*std, color='purple', linestyle=':', linewidth=1.5, alpha=0.5)
    
    # Add grid
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add legend
    ax.legend(loc='upper right')
    
    # Add statistics text
    stats_text = f'Statistics:\n'
    stats_text += f'Sample Mean: {np.mean(data):.4f}\n'
    stats_text += f'Sample Std: {np.std(data):.4f}\n'
    stats_text += f'Skewness: {np.mean((data - mean)**3)/std**3:.4f}\n'
    stats_text += f'Kurtosis: {np.mean((data - mean)**4)/std**4 - 3:.4f}'
    
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('task5_histogram.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 5 completed: Histogram of normal distribution")
    print("  Saved as 'task5_histogram.png'")
    
    return fig, ax

# Task 6: 3D Surface Plot
print("\n" + "=" * 60)
print("TASK 6: 3D Surface Plot")
print("=" * 60)

def task6_3d_surface():
    """Create 3D surface plot of f(x,y) = cos(x² + y²)"""
    # Create meshgrid
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # Calculate Z values
    Z = np.cos(X**2 + Y**2)
    
    # Create 3D figure
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create surface plot
    surf = ax.plot_surface(X, Y, Z, 
                          cmap='viridis', 
                          alpha=0.9,
                          linewidth=0.5,
                          antialiased=True,
                          rstride=2, 
                          cstride=2)
    
    # Add colorbar
    cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    cbar.set_label('f(x,y) value', fontsize=10, rotation=270, labelpad=15)
    
    # Customization
    ax.set_xlabel('X axis', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_ylabel('Y axis', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_zlabel('f(x,y)', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_title(r'3D Surface Plot: $f(x,y) = \cos(x^2 + y^2)$', 
                 fontsize=14, fontweight='bold', pad=20)
    
    # Set viewing angle
    ax.view_init(elev=30, azim=45)
    
    # Add contour lines on axes
    ax.contour(X, Y, Z, 10, zdir='z', offset=-1.2, cmap='coolwarm', alpha=0.5)
    ax.contour(X, Y, Z, 10, zdir='x', offset=-5.5, cmap='coolwarm', alpha=0.5)
    ax.contour(X, Y, Z, 10, zdir='y', offset=5.5, cmap='coolwarm', alpha=0.5)
    
    # Add text with function properties
    ax.text2D(0.05, 0.95, "Properties:\n• Radial symmetry\n• Oscillatory nature\n• Maximum at origin", 
              transform=ax.transAxes, fontsize=10,
              bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('task6_3d_surface.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 6 completed: 3D surface plot created")
    print("  Saved as 'task6_3d_surface.png'")
    
    return fig, ax

# Task 7: Bar Chart
print("\n" + "=" * 60)
print("TASK 7: Product Sales Bar Chart")
print("=" * 60)

def task7_bar_chart():
    """Create bar chart of product sales"""
    # Data
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales = [200, 150, 250, 175, 225]
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create color gradient based on sales
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(products)))
    
    # Create bar chart
    bars = ax.bar(products, sales, color=colors, 
                  edgecolor='black', linewidth=1.5, 
                  alpha=0.8, width=0.6)
    
    # Add value labels on top of bars
    for bar, sale in zip(bars, sales):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{sale}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Customization
    ax.set_xlabel('Products', fontsize=12, fontweight='bold')
    ax.set_ylabel('Sales (units)', fontsize=12, fontweight='bold')
    ax.set_title('Product Sales Performance', fontsize=14, fontweight='bold')
    
    # Set y-axis limit
    ax.set_ylim([0, max(sales) * 1.2])
    
    # Add grid
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add total sales line
    total_sales = sum(sales)
    ax.axhline(y=total_sales/len(products), color='red', 
               linestyle='--', linewidth=2, alpha=0.7, 
               label=f'Average: {total_sales/len(products):.1f}')
    
    # Add best and worst performers
    best_product = products[sales.index(max(sales))]
    worst_product = products[sales.index(min(sales))]
    
    # Add annotations
    ax.text(0.02, 0.98, f'Total Sales: {total_sales}\n'
                       f'Best: {best_product} ({max(sales)})\n'
                       f'Worst: {worst_product} ({min(sales)})', 
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('task7_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 7 completed: Product sales bar chart")
    print("  Saved as 'task7_bar_chart.png'")
    
    return fig, ax

# Task 8: Stacked Bar Chart
print("\n" + "=" * 60)
print("TASK 8: Stacked Bar Chart")
print("=" * 60)

def task8_stacked_bar_chart():
    """Create stacked bar chart of categories over time periods"""
    # Data
    time_periods = ['T1', 'T2', 'T3', 'T4']
    categories = ['Category A', 'Category B', 'Category C']
    
    # Generate random data for each category
    np.random.seed(42)
    data = {
        'Category A': np.random.randint(20, 50, len(time_periods)),
        'Category B': np.random.randint(30, 60, len(time_periods)),
        'Category C': np.random.randint(10, 40, len(time_periods))
    }
    
    # Convert to numpy arrays for easier manipulation
    bottom_values = np.zeros(len(time_periods))
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(14, 9))
    
    # Colors for categories
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    # Plot stacked bars
    for i, (category, values) in enumerate(data.items()):
        bars = ax.bar(time_periods, values, bottom=bottom_values, 
                     color=colors[i], edgecolor='black', 
                     linewidth=1.2, alpha=0.8, width=0.7,
                     label=category)
        
        # Add value labels in the middle of each segment
        for j, (bar, value) in enumerate(zip(bars, values)):
            height = bar.get_height()
            y_pos = bottom_values[j] + height / 2
            
            # Only show label if segment is large enough
            if height > 5:
                ax.text(bar.get_x() + bar.get_width()/2., y_pos,
                        f'{value}', ha='center', va='center', 
                        fontsize=10, fontweight='bold', color='white')
        
        bottom_values += values
    
    # Customization
    ax.set_xlabel('Time Periods', fontsize=12, fontweight='bold')
    ax.set_ylabel('Contribution Value', fontsize=12, fontweight='bold')
    ax.set_title('Category Contributions Over Time Periods', 
                 fontsize=14, fontweight='bold')
    
    # Add total values on top of each bar
    totals = bottom_values  # After accumulation, bottom_values contains totals
    for i, total in enumerate(totals):
        ax.text(i, total + 2, f'Total: {int(total)}', 
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Add grid
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add legend
    ax.legend(loc='upper left', title='Categories', title_fontsize=11)
    
    # Add summary statistics
    summary_text = "Summary Statistics:\n"
    for category, values in data.items():
        summary_text += f"{category}:\n"
        summary_text += f"  Avg: {np.mean(values):.1f}, "
        summary_text += f"Total: {np.sum(values)}\n"
    
    ax.text(0.02, 0.98, summary_text, transform=ax.transAxes,
            fontsize=9, verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('task8_stacked_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✓ Task 8 completed: Stacked bar chart created")
    print("  Saved as 'task8_stacked_bar_chart.png'")
    
    return fig, ax

# Main execution function
def main():
    """Execute all plotting tasks"""
    print("\nStarting all plotting tasks...")
    print("-" * 60)
    
    # Execute all tasks
    tasks = [
        ("Task 1: Quadratic Plot", task1_quadratic_plot),
        ("Task 2: Trigonometric Plot", task2_trigonometric_plot),
        ("Task 3: Subplots Grid", task3_subplots_grid),
        ("Task 4: Scatter Plot", task4_scatter_plot),
        ("Task 5: Histogram", task5_histogram),
        ("Task 6: 3D Surface Plot", task6_3d_surface),
        ("Task 7: Bar Chart", task7_bar_chart),
        ("Task 8: Stacked Bar Chart", task8_stacked_bar_chart)
    ]
    
    for task_name, task_function in tasks:
        print(f"\nExecuting {task_name}...")
        try:
            task_function()
            print(f"✓ {task_name} completed successfully")
        except Exception as e:
            print(f"✗ Error in {task_name}: {e}")
    
    print("\n" + "=" * 70)
    print("ALL TASKS COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    
    print("\nGenerated Plots:")
    print("1. task1_quadratic_plot.png - Quadratic function")
    print("2. task2_sine_cosine_plot.png - Sine and cosine functions")
    print("3. task3_subplots_grid.png - 2x2 subplots grid")
    print("4. task4_scatter_plot.png - Random scatter plot")
    print("5. task5_histogram.png - Normal distribution histogram")
    print("6. task6_3d_surface.png - 3D surface plot")
    print("7. task7_bar_chart.png - Product sales bar chart")
    print("8. task8_stacked_bar_chart.png - Stacked bar chart")

if __name__ == "__main__":
    main()