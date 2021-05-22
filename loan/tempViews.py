class LoanCollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Loancollentionsheet
    template_name = "loan/loan-collection-update.html"
    form_class = LoanCollectionUpdateForm
    success_url = "/loan"

    def get_object(self, *args, **kwargs):
        id_from_url = self.kwargs.get("loan_collection_id")
        collection = Loancollentionsheet.objects.get(loan_collection_id=id_from_url)
        return collection

    # def post(self, request, loan_collection_id, *args, **kwargs):
    #     collection = self.get_object()
    #     new_update = Loancollentionsheet.objects.get(
    #         loan_collection_id=collection.loan_collection_id
    #     )
    #     collection_form = LoanCollectionUpdateForm(request.POST, instance=new_update)
    #     if collection_form.is_valid():
    #         data = collection_form.cleaned_data
    #         deposite_amount = data["loan_deposite_amount"]
    #         withdrawal_amount = data["loan_deposite_withdrawal"]
    #         collection_amount = data["loan_collection_installment_amount"]

    #         collection = self.get_object()
    #         new_update = Loancollentionsheet.objects.get(
    #             loan_collection_id=collection.loan_collection_id
    #         )
    #         if deposite_amount > Money(0, "BDT"):
    #             new_update.add_loan_deposite()

    #         if withdrawal_amount > Money(0, "BDT"):
    #             new_update.loan_withdrawal_func()

    #         if collection_amount:
    #             if new_update.check_loan_collection_possibility():
    #                 new_update.add_loan_collection_installment_amount()
    #         collection_form.save()
    #         return render(request, "loan/loan-home.html")

    # def get(self, request, loan_collection_id, *args, **kwargs):
    #     collection = self.get_object()
    #     new_update = Loancollentionsheet.objects.get(
    #         loan_collection_id=collection.loan_collection_id
    #     )
    #     collection_form = LoanCollectionUpdateForm(request.POST, instance=new_update)
    #     context = {"collection_form": collection_form}
    #     return render(request, "loan/loan-collection-update.html", context)

    def form_valid(self, form):
        # (
        #     deposite_amount,
        #     withdrawal_amount,
        #     collection_amount,
        # ) = self.post()  # list unpacking

        data = form.cleaned_data
        deposite_amount = data["loan_deposite_amount"]
        withdrawal_amount = data["loan_deposite_withdrawal"]
        collection_amount = data["loan_collection_installment_amount"]

        collection = self.get_object()
        new_update = Loancollentionsheet.objects.get(
            loan_collection_id=collection.loan_collection_id
        )
        if deposite_amount > Money(0, "BDT"):
            new_update.add_loan_deposite()

        if withdrawal_amount > Money(0, "BDT"):
            new_update.loan_withdrawal_func()

        if collection_amount:
            if new_update.check_loan_collection_possibility():
                new_update.add_loan_collection_installment_amount()
        new_update.save()

        return super().form_valid(form)