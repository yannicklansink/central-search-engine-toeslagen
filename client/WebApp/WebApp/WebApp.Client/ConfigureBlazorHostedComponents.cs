namespace WebApp.Client
{
    public static class ServiceCollectionExtensions
    {
        public static IServiceCollection ConfigureBlazorHostedComponents(this IServiceCollection services, string baseAddress)
        {
            services.AddAuthorizationCore();

            services.AddBASUIBlazor(options =>
            {
                options.ShowDialogForUncaughtExceptions();
                options.UseDefaultFormValidatorComponent<Blazored.FluentValidation.FluentValidationValidator>();

                Components.InputsBinding.Demo.ConfigureBASUIBlazor(options);
                Components.InputsDefaults.Demo.ConfigureBASUIBlazor(options);
            });

            services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(baseAddress) });

            return services;
        }
    }

}
